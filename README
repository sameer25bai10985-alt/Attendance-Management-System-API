# Screenshots

This folder contains **mockup / expected-result images** for each key endpoint, generated to
show the documented request and response shape (method, URL, request body, status code, and
response JSON) exactly as implemented in `routes/*.py` and `models/*.py`.

**These are illustrations, not live captures** — they were not produced by hitting a running
server against a real MySQL database. Each image is watermarked with a footer note saying so.
Before final submission, it's worth replacing them with real Postman screenshots captured
against your own running instance (see **Testing Instructions → Manual / live testing** in the
main `README.md`), since a grader may expect genuine captures rather than mockups.

| File | Endpoint | Scenario |
|---|---|---|
| `01-create-subject.png` | `POST /subjects` | Successful subject creation |
| `02-get-subjects.png` | `GET /subjects` | List of subjects |
| `03-mark-attendance.png` | `POST /attendance` | Successful attendance marking |
| `04-duplicate-attendance.png` | `POST /attendance` | Duplicate request rejected (400) |
| `05-attendance-by-student.png` | `GET /attendance/student/{id}` | Attendance history for a student |
| `06-attendance-by-date.png` | `GET /attendance/date/{date}` | Date-wise attendance |
| `07-overall-percentage.png` | `GET /attendance/percentage/student/{id}` | Overall attendance percentage |
| `08-subject-percentage.png` | `GET /attendance/percentage/student/{id}/subject/{id}` | Subject-wise attendance percentage |

To regenerate real screenshots: run the server locally (`python app.py`) against a live MySQL
database, send each request above in Postman, and export/screenshot the response, replacing the
matching file in this folder.

