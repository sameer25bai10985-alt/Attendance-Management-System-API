# Attendance Management System API — Project Report

## 1. Cover Page
**Project Title:** Attendance Management System API  
**Student:** Sameer Yadav  
**Course:** Build Your Own Project / VITyarthi  

## 2. Introduction
Attendance is an important academic record in educational institutions. Manual attendance systems require repeated record keeping and make it difficult to retrieve data or calculate attendance percentage quickly. This project implements a backend REST API that stores attendance information in MySQL and exposes operations through Flask endpoints.

## 3. Problem Statement
Manual attendance recording can be slow, repetitive, and prone to duplicate entries and calculation mistakes. The project provides a structured API-based solution for creating subjects, recording attendance, retrieving records, and calculating attendance percentages.

## 4. Functional Requirements
- Create and retrieve subjects.
- Mark student attendance as present or absent.
- Prevent duplicate attendance for the same student, subject, and date.
- Retrieve attendance by student.
- Retrieve attendance by date.
- Calculate overall attendance percentage.
- Calculate subject-wise attendance percentage.

## 5. Non-Functional Requirements
- Performance: fast response for normal classroom data.
- Security: protect database credentials.
- Usability: simple REST endpoints and JSON.
- Reliability: constraints and validation maintain data correctness.
- Maintainability: modular routes/models/database structure.
- Error handling: invalid or duplicate requests return meaningful errors.

## 6. System Architecture
See `docs/architecture.md`.

## 7. Design Diagrams
- Use Case: `docs/use_case.md`
- Workflow: `docs/workflow.md`
- Sequence: `docs/sequence_diagram.md`
- Component: `docs/component_diagram.md`
- ER Diagram: `docs/er_diagram.md`

## 8. Design Decisions & Rationale
See `docs/design_decisions.md`.

## 9. Implementation Details
The backend is implemented in Python using Flask. HTTP routes accept JSON requests and call model/database functions. MySQL stores subjects and attendance records. A unique database constraint prevents duplicate student-subject-date attendance entries.

## 10. Screenshots / Results
Add Postman screenshots showing:
1. Subject creation
2. Subject retrieval
3. Attendance marking
4. Duplicate attendance rejection
5. Student-wise retrieval
6. Date-wise retrieval
7. Overall percentage
8. Subject-wise percentage

## 11. Testing Approach
Testing includes valid API requests, missing-field validation, duplicate attendance validation, retrieval operations, and attendance percentage verification. The included `tests/test_api.py` provides basic integration tests for a running local server.

## 12. Challenges Faced
- Designing database tables for attendance data.
- Preventing duplicate attendance records.
- Connecting Flask with MySQL.
- Returning correct HTTP responses for invalid data.
- Calculating attendance percentage from database records.

## 13. Learnings & Key Takeaways
- REST API design using Flask.
- MySQL database connectivity and constraints.
- Modular backend programming.
- Input validation and error handling.
- API testing using Postman.
- Git and GitHub version control.

## 14. Future Enhancements
- Student profile management.
- Teacher/admin authentication.
- Web dashboard.
- Low-attendance alerts.
- Monthly reports and PDF/CSV export.
- QR-code or biometric attendance.
- Cloud deployment.

## 15. References
- Flask Documentation
- MySQL Documentation
- Python Documentation
- Postman Documentation
