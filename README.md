# Library-management-system-project
# Attendance Management System API
## Project Overview
This project is a Backend REST API for managing student attendance.

It allows:
* Managing subjects
* Marking daily attendance for students
* Preventing duplicate attendance for the same student, subject, and date
* Fetching attendance records
* Calculating attendance percentage (overall & subject-wise)

This project focuses on backend fundamentals, clean API design, validation, and SQL-based data handling.

## Tech Stack
* Python
* Flask
* MySQL
* Postman (API testing)

## Project Structure
```
Attendance-Management-System-API/
│
├── app.py                    # Application entry point
├── db.py                     # MySQL database connection
├── models/
│   ├── __init__.py
│   ├── subject.py            # Subject database operations
│   └── attendance.py         # Attendance database operations
├── routes/
│   ├── __init__.py
│   ├── subject_routes.py     # Subject-related routes
│   └── attendance_routes.py  # Attendance-related routes
├── requirements.txt
├── README.md
└── screenshots/              # Postman API testing screenshots
 ```

## Setup Instructions
### 1️ Clone the repository
```
git clone https://github.com/iamajaykr06/Attendance-Management-System-API.git
cd Attendance-Management-System-API
```

### 2️ Create virtual environment (recommended)
```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3 Install dependencies
```
pip install -r requirements.txt
```

## ️Database Setup
### Create Database
```
CREATE DATABASE attendance_db;
```

### Create Subjects Table
```
CREATE TABLE subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(50) NOT NULL UNIQUE
);
```

### Create Attendance Table
```
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
Note: Student records are assumed to exist and are referenced using `student_id`.

The UNIQUE constraint ensures attendance cannot be marked twice for the same student, subject, and date.

## Update Database Credentials
Edit `db.py` and update:
* MySQL username
* Password
* Database name

## Run the Application
```
python app.py
```

Server runs at:
```http://127.0.0.1:5000```

## API Endpoints
### Create Subject

**POST** `/subjects`
```
{
  "name": "Software Engineering",
  "code": "CS101"
}
```

Responses
- `201 Created`
- `400 Bad Request`

Example error response:
```
{
  "message": "Attendance already marked or invalid data"
}
```
## Get All Subjects
**GET** `/subjects`

## Mark Attendance
**POST** `/attendance`
```
{
  "student_id": 1,
  "subject_id": 1,
  "attendance_date": "2026-01-12",
  "status": "present"
}
```

### Responses
- `201 Created`
- `400 Bad Request` (duplicate or invalid data)

## Get Attendance by Student
**GET** `/attendance/student/{student_id}`

## Get Attendance by Date
**GET** `/attendance/date/{date}`

## Attendance Percentage (Overall)
**GET** `/attendance/percentage/student/{student_id}`
### Response
```
{
  "student_id": 1,
  "attendance_percentage": "100.00"
}
```

## Attendance Percentage (Subject-wise)
**GET** `/attendance/percentage/student/{student_id}/subject/{subject_id}`
### Response
```
{
  "student_id": 1,
  "subject_id": 1,
  "attendance_percentage": "100.00"
}
```

## Screenshots
All API request & response screenshots (tested using Postman) are available in the screenshots/ directory, including:
- Subject creation
- Attendance marking
- Duplicate attendance validation
- Attendance retrieval
- Attendance percentage calculation

## Features Implemented
- Subject management
- Attendance marking with duplicate prevention
- Date-wise and student-wise attendance retrieval
- Attendance percentage calculation
- Input validation
- Proper HTTP status codes
- Clean project structure

## Learning Outcomes
- REST API design using Flask
- SQL constraints for data integrity
- Backend validation strategies
- Attendance calculation logic
- Clean separation of routes and models

## Author
Ajay Kumar
