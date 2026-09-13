# Attendance Management System API

## Project Overview
Attendance Management System API is a backend REST API developed using **Python, Flask, and MySQL**. It provides a structured way to manage subjects and student attendance records. The system supports attendance marking, duplicate-entry prevention, attendance retrieval, and percentage calculation.

The project demonstrates REST API design, database connectivity, validation, modular programming, and SQL-based data handling.

## Objectives
- Digitize student attendance recording.
- Reduce duplicate and incorrect attendance entries.
- Store attendance records in a structured MySQL database.
- Retrieve attendance by student and date.
- Calculate overall and subject-wise attendance percentage.
- Apply modular Flask development and REST principles.

## Major Functional Modules
### 1. Subject Management
Creates and retrieves academic subjects using subject name and subject code.

### 2. Attendance Management
Marks a student as present or absent for a selected subject and date while preventing duplicate attendance.

### 3. Attendance Reporting and Percentage
Retrieves attendance history and calculates overall or subject-wise attendance percentage.

## Features
- Create subjects
- View subjects
- Mark student attendance
- Prevent duplicate attendance for the same student, subject, and date
- View attendance by student
- View attendance by date
- Calculate overall attendance percentage
- Calculate subject-wise attendance percentage
- Validate request data
- Return meaningful HTTP status codes

## Input and Output Structure
The API accepts JSON input through HTTP requests and returns JSON output.

Example attendance input:
```json
{
  "student_id": 1,
  "subject_id": 1,
  "attendance_date": "2026-09-13",
  "status": "present"
}
```

Example percentage output:
```json
{
  "student_id": 1,
  "attendance_percentage": "75.00"
}
```

## Non-Functional Requirements
1. **Performance:** Common API operations should respond quickly for normal classroom-sized datasets.
2. **Security:** Database credentials should not be exposed publicly and should be moved to environment variables for deployment.
3. **Usability:** API endpoints and JSON formats are kept simple and consistent.
4. **Reliability:** Database constraints and validation reduce invalid or duplicate records.
5. **Maintainability:** Routes, models, and database code are separated into modules.
6. **Error Handling:** Invalid input and duplicate attendance produce appropriate error responses.

## Technology Stack
- Python
- Flask
- MySQL
- MySQL Connector for Python
- Postman for API testing
- Git and GitHub for version control

## Recommended Project Structure
```text
Attendance-Management-System-API/
├── app.py
├── db.py
├── requirements.txt
├── README.md
├── statement.md
├── models/
│   ├── __init__.py
│   ├── subject.py
│   └── attendance.py
├── routes/
│   ├── __init__.py
│   ├── subject_routes.py
│   └── attendance_routes.py
├── tests/
│   └── test_api.py
├── docs/
│   ├── architecture.md
│   ├── workflow.md
│   ├── use_case.md
│   ├── sequence_diagram.md
│   ├── component_diagram.md
│   ├── er_diagram.md
│   └── design_decisions.md
└── screenshots/
```

## Database Setup
Create the database:
```sql
CREATE DATABASE attendance_db;
USE attendance_db;
```

Create the subjects table:
```sql
CREATE TABLE subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(50) NOT NULL UNIQUE
);
```

Create the attendance table:
```sql
CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    status ENUM('present', 'absent') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(student_id, subject_id, attendance_date)
);
```

## Installation and Running
1. Clone your repository.
```bash
git clone https://github.com/sameer25bai10985-alt/Library-management-system-project.git
cd Library-management-system-project
```

2. Create and activate a virtual environment.
```bash
python -m venv venv
```
Windows:
```bash
venv\Scripts\activate
```
Linux/macOS:
```bash
source venv/bin/activate
```

3. Install dependencies.
```bash
pip install -r requirements.txt
```

4. Configure MySQL credentials in `db.py`.

5. Run the Flask application.
```bash
python app.py
```

Default development URL:
```text
http://127.0.0.1:5000
```

## Main API Endpoints
| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/subjects` | Create a subject |
| GET | `/subjects` | Get all subjects |
| POST | `/attendance` | Mark attendance |
| GET | `/attendance/student/{student_id}` | Get attendance of a student |
| GET | `/attendance/date/{date}` | Get attendance for a date |
| GET | `/attendance/percentage/student/{student_id}` | Overall percentage |
| GET | `/attendance/percentage/student/{student_id}/subject/{subject_id}` | Subject-wise percentage |

## Testing Instructions
1. Start MySQL and create the required database/tables.
2. Run the Flask server using `python app.py`.
3. Run:
```bash
python tests/test_api.py
```
4. APIs can also be tested manually in Postman.
5. Capture screenshots for successful subject creation, attendance marking, duplicate validation, retrieval, and percentage calculation.

## Expected Validation Tests
- Missing required JSON fields should be rejected.
- Duplicate attendance for the same student, subject, and date should be rejected.
- Invalid attendance status should be rejected.
- Valid attendance should be stored successfully.
- Attendance percentage should be calculated from stored records.

## Design Documentation
The `docs/` folder contains architecture, workflow, use-case, sequence, component, ER, and design-decision documentation.

## Screenshots
Store Postman screenshots in the `screenshots/` folder. Recommended screenshots:
- Create subject
- Get subjects
- Mark attendance
- Duplicate attendance error
- Student attendance history
- Date-wise attendance
- Overall percentage
- Subject-wise percentage

## Limitations
- Student details are currently represented by `student_id` rather than a complete student-management module.
- No login or role-based authentication is included.
- No graphical frontend is included.
- Database credentials may require manual configuration.

## Future Enhancements
- Student management module
- Teacher/admin login and authentication
- Web dashboard
- Low-attendance alerts
- Monthly attendance reports
- CSV/PDF export
- QR-code or biometric attendance integration
- Cloud deployment

## Learning Outcomes
- REST API development using Flask
- MySQL database connectivity
- CRUD/data operations
- Validation and SQL constraints
- Modular backend design
- API testing with Postman
- Git/GitHub version control

## Author
Sameer Yadav
