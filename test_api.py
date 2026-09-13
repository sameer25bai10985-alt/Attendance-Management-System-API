"""
Test suite for the Attendance Management System API.

These are unit-style tests that use Flask's test client and mock
`db.get_db_connection` so they can run WITHOUT a live MySQL server
(useful for CI / grading). For a full end-to-end check against a real
MySQL database, follow the "Live integration testing" section in the
README instead and exercise the endpoints with Postman.

Run with:
    python -m pytest tests/test_api.py -v
or:
    python tests/test_api.py
"""

import os
import sys
import unittest
from unittest.mock import patch, MagicMock

# Make the project root importable when running this file directly.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app  # noqa: E402


def make_mock_connection(fetchone_return=None, fetchall_return=None, rowcount=1, raise_on_execute=None):
    """Builds a fake mysql.connector connection/cursor pair."""
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = fetchone_return
    mock_cursor.fetchall.return_value = fetchall_return or []
    mock_cursor.rowcount = rowcount

    if raise_on_execute:
        mock_cursor.execute.side_effect = raise_on_execute

    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    return mock_conn, mock_cursor


class SubjectApiTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    @patch("models.subject.get_db_connection")
    def test_create_subject_success(self, mock_get_conn):
        mock_conn, _ = make_mock_connection()
        mock_get_conn.return_value = mock_conn

        response = self.client.post("/subjects", json={"name": "Data Structures", "code": "CS201"})
        self.assertEqual(response.status_code, 201)

    @patch("models.subject.get_db_connection")
    def test_get_all_subjects(self, mock_get_conn):
        rows = [{"id": 1, "name": "Data Structures", "code": "CS201"}]
        mock_conn, _ = make_mock_connection(fetchall_return=rows)
        mock_get_conn.return_value = mock_conn

        response = self.client.get("/subjects")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["data"], rows)


class AttendanceApiTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_mark_attendance_missing_field_returns_400(self):
        # No mocking needed: validation happens before the DB is touched.
        response = self.client.post("/attendance", json={"student_id": 1, "subject_id": 1})
        self.assertEqual(response.status_code, 400)
        self.assertIn("missing", response.get_json()["message"])

    def test_mark_attendance_empty_field_returns_400(self):
        response = self.client.post(
            "/attendance",
            json={"student_id": 1, "subject_id": 1, "attendance_date": "", "status": "present"},
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("cannot be empty", response.get_json()["message"])

    def test_mark_attendance_non_json_body_returns_error(self):
        # Flask/Werkzeug rejects a non-JSON content-type with 415 before the
        # route's own "Request must be JSON" 400 branch is ever reached.
        response = self.client.post("/attendance", data="not json", content_type="text/plain")
        self.assertEqual(response.status_code, 415)

    @patch("models.attendance.get_db_connection")
    def test_mark_attendance_success(self, mock_get_conn):
        mock_conn, _ = make_mock_connection()
        mock_get_conn.return_value = mock_conn

        response = self.client.post(
            "/attendance",
            json={
                "student_id": 1,
                "subject_id": 1,
                "attendance_date": "2026-09-13",
                "status": "present",
            },
        )
        self.assertEqual(response.status_code, 201)

    @patch("models.attendance.get_db_connection")
    def test_mark_attendance_duplicate_rejected(self, mock_get_conn):
        # Simulate the UNIQUE constraint firing on a duplicate insert.
        mock_conn, _ = make_mock_connection(raise_on_execute=Exception("Duplicate entry"))
        mock_get_conn.return_value = mock_conn

        response = self.client.post(
            "/attendance",
            json={
                "student_id": 1,
                "subject_id": 1,
                "attendance_date": "2026-09-13",
                "status": "present",
            },
        )
        self.assertEqual(response.status_code, 400)

    @patch("models.attendance.get_db_connection")
    def test_attendance_percentage_no_records_returns_404(self, mock_get_conn):
        mock_conn, _ = make_mock_connection(fetchall_return=[])
        mock_get_conn.return_value = mock_conn

        response = self.client.get("/attendance/percentage/student/999")
        self.assertEqual(response.status_code, 404)


class StudentApiTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_student_missing_field_returns_400(self):
        response = self.client.post("/students", json={"name": "Asha Rao"})
        self.assertEqual(response.status_code, 400)

    @patch("models.student.get_db_connection")
    def test_create_student_success(self, mock_get_conn):
        mock_conn, _ = make_mock_connection()
        mock_get_conn.return_value = mock_conn

        response = self.client.post(
            "/students",
            json={"name": "Asha Rao", "roll_no": "21CS045", "email": "asha@example.com", "branch": "CSE"},
        )
        self.assertEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()
