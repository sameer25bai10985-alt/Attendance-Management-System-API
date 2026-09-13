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

### 2. Student Management
Creates, retrieves, updates, deletes, and searches student records (name, roll number, email, branch).

### 3. Attendance Management
Marks a student as present or absent for a selected subject and date while preventing duplicate attendance.

### 4. Attendance Reporting and Percentage
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

## Project Structure
```text
Attendance-Management-System-API/
├── app.py
├── db.py
├── requirements.txt
├── README.md
├── statement.md
├── PROJECT_REPORT.md
├── .env.example
├── .gitignore
├── models/
│   ├── __init__.py
│   ├── subject.py
│   ├── student.py
│   └── attendance.py
├── routes/
│   ├── __init__.py
│   ├── subject_routes.py
│   ├── student_routes.py
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
    ├── README.md
    └── 01-create-subject.png ... 08-subject-percentage.png
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

Create the students table:
```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_no VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    branch VARCHAR(100) NOT NULL
);
```

## Installation and Running
1. Clone your repository.
```bash
git clone https://github.com/sameer25bai10985-alt/Attendance-Management-System-API.git
cd Attendance-Management-System-API
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

4. Configure MySQL credentials as environment variables (copy `.env.example` to `.env` and fill in your values, or export them directly):
```bash
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password_here
DB_NAME=attendance_db
```

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
| GET | `/subjects/{subject_id}` | Get a subject by ID |
| PUT | `/subjects/{subject_id}` | Update a subject |
| DELETE | `/subjects/{subject_id}` | Delete a subject |
| POST | `/attendance` | Mark attendance |
| GET | `/attendance/student/{student_id}` | Get attendance of a student |
| GET | `/attendance/date/{date}` | Get attendance for a date |
| GET | `/attendance/percentage/student/{student_id}` | Overall percentage |
| GET | `/attendance/percentage/student/{student_id}/subject/{subject_id}` | Subject-wise percentage |
| POST | `/students` | Create a student |
| GET | `/students` | Get all students |
| GET | `/students/{student_id}` | Get a student by ID |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |
| GET | `/students/search` | Search students |

## Testing Instructions

### Automated tests (no live database needed)
The test suite mocks the database layer, so it can run without MySQL being set up:
```bash
python -m pytest tests/test_api.py -v
```
This covers validation (missing/empty fields), successful create/mark flows, duplicate-attendance
rejection, and not-found/no-records responses.

### Manual / live testing (with a real MySQL database)
1. Start MySQL and create the required database/tables (see **Database Setup** above).
2. Set the `DB_*` environment variables (see **Installation and Running**).
3. Run the Flask server using `python app.py`.
4. Exercise the endpoints in Postman.
5. Capture screenshots for successful subject creation, attendance marking, duplicate validation, retrieval, and percentage calculation, and save them in `screenshots/` (see `screenshots/README.md`).

## Expected Validation Tests
- Missing required JSON fields should be rejected.
- Duplicate attendance for the same student, subject, and date should be rejected.
- Invalid attendance status should be rejected.
- Valid attendance should be stored successfully.
- Attendance percentage should be calculated from stored records.

## Design Documentation
The `docs/` folder contains architecture, workflow, use-case, sequence, component, ER, and design-decision documentation.

## Screenshots
Mockup images showing the expected request/response for each key endpoint are stored in
`screenshots/` (see `screenshots/README.md` for the full list and an explanation — these are
illustrations of the documented API contract, not live captures against a running server):

![Create subject](screenshots/01-create-subject.png)
![Mark attendance duplicate rejected](screenshots/04-duplicate-attendance.png)
![Overall attendance percentage](screenshots/07-overall-percentage.png)

## Limitations
- No login or role-based authentication is included.
- No graphical frontend is included.
- `student_id`/`subject_id` in the `attendance` table are not enforced with database-level foreign-key constraints yet.
- Database credentials must be configured via environment variables before running.

## Future Enhancements
- Foreign-key constraints between attendance and students/subjects
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
