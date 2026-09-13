from flask import Blueprint,jsonify,request
from models.attendance import (mark_attendance,
                               get_attendance_by_student,
                               get_attendance_by_date,
                               get_attendance_percentage_overall,
                               get_attendance_percentage_subject)

attendance_bp = Blueprint("attendance",__name__)

@attendance_bp.route("/attendance", methods=["POST"])
def mark_attendance_route():
    data = request.get_json()

    if data is None:
        return jsonify({"message": "Request must be JSON"}), 400

    required_fields = [
        "student_id",
        "subject_id",
        "attendance_date",
        "status"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"attribute {field} missing"}), 400

        if str(data[field]).strip() == "":
            return jsonify({"message": f"attribute {field} cannot be empty"}), 400

    saved = mark_attendance(data)

    if not saved:
        return jsonify({"message": "Attendance already marked or invalid data"}), 400

    return jsonify({
        "message": "Attendance marked successfully"
    }), 201

@attendance_bp.route("/attendance/student/<int:student_id>", methods=["GET"])
def get_attendance_by_student_route(student_id):
    records = get_attendance_by_student(student_id)

    if records is None:
        return jsonify({"message": "Failed to fetch attendance"}), 500

    return jsonify({
        "data": records
    }), 200

@attendance_bp.route("/attendance/date/<attendance_date>", methods=["GET"])
def get_attendance_by_date_route(attendance_date):
    records = get_attendance_by_date(attendance_date)

    if records is None:
        return jsonify({"message": "Failed to fetch attendance"}), 500

    return jsonify({
        "data": records
    }), 200

@attendance_bp.route("/attendance/percentage/student/<int:student_id>", methods=["GET"])
def attendance_percentage_overall_route(student_id):
    percentage = get_attendance_percentage_overall(student_id)

    if percentage is None:
        return jsonify({"message": "No attendance records found"}), 404

    return jsonify({
        "student_id": student_id,
        "attendance_percentage": percentage
    }), 200

@attendance_bp.route(
    "/attendance/percentage/student/<int:student_id>/subject/<int:subject_id>",
    methods=["GET"]
)
def attendance_percentage_subject_route(student_id, subject_id):
    percentage = get_attendance_percentage_subject(student_id, subject_id)

    if percentage is None:
        return jsonify({"message": "No attendance records found"}), 404

    return jsonify({
        "student_id": student_id,
        "subject_id": subject_id,
        "attendance_percentage": percentage
    }), 200
