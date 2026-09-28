# Attendance Management System API (Java / Spring Boot)

A REST API for managing students, subjects, attendance records and attendance percentages.
This is the Java version of the original Python/Flask project. All endpoints, JSON field names
(`roll_no`, `student_id`, `attendance_date` ...) and response shapes are kept the same, so your
Postman collection keeps working.

## Tech stack

| Technology | Use |
|---|---|
| Java 17+ | Language |
| Spring Boot 3.3 (Web) | REST controllers |
| Spring Data JPA / Hibernate | Database access (replaces raw SQL in `db.py`) |
| Bean Validation | Required-field checks (replaces the `required_fields` loops) |
| MySQL 8 | Database |
| JUnit 5, Mockito, MockMvc | Tests |
| Maven | Build tool |

## Project structure

```
src/main/java/com/attendance/
├── AttendanceApplication.java        # entry point (was app.py)
├── controller/                       # HTTP layer (was *_routes.py)
│   ├── StudentController.java
│   ├── SubjectController.java
│   └── AttendanceController.java
├── service/                          # business logic
│   ├── StudentService.java
│   ├── SubjectService.java
│   └── AttendanceService.java
├── repository/                       # database access (was student.py / subject.py / attendance.py / db.py)
├── model/                            # JPA entities = database tables
├── dto/                              # request / response objects
└── exception/                        # error handling -> JSON error messages
src/main/resources/application.properties
src/test/java/...                     # unit + controller tests
docs/schema.sql                       # optional manual schema
```

Layers: **Controller → Service → Repository → MySQL**.

## Setup & run

1. **Install** JDK 17 or newer and Maven 3.9+ (or open the project in IntelliJ / Eclipse / VS Code).
2. **Start MySQL** – either your own install, or `docker compose up -d` (uses password `root123`).
3. **Set the database details** as environment variables (see `.env.example`):

   ```bash
   # Linux / macOS
   export DB_USER=root
   export DB_PASSWORD=root123
   # Windows PowerShell
   $env:DB_USER="root"; $env:DB_PASSWORD="root123"
   ```
   Defaults: host `localhost`, port `3306`, database `attendance_db` (created automatically), user `root`.
4. **Run**

   ```bash
   mvn spring-boot:run
   ```
   API is available at `http://localhost:8080`. Tables are created automatically on first start.
5. **Test**: `mvn test` (no database needed – tests use mocks).
6. **Build a jar**: `mvn clean package` then `java -jar target/attendance-management-system-api-1.0.0.jar`.

## Endpoints

| Method | URL | Description | Success |
|---|---|---|---|
| POST | `/students` | Create student | 201 |
| GET | `/students` | List students | 200 |
| GET | `/students/{id}` | Get one student | 200 / 404 |
| PUT | `/students/{id}` | Update student | 200 / 404 |
| DELETE | `/students/{id}` | Delete student (and their attendance) | 200 / 404 |
| GET | `/students/search?keyword=` | Search name / roll_no / email / branch | 200 |
| POST | `/subjects` | Create subject | 201 |
| GET | `/subjects` | List subjects | 200 |
| GET | `/subjects/{id}` | Get one subject | 200 / 404 |
| PUT | `/subjects/{id}` | Update subject | 200 / 404 |
| DELETE | `/subjects/{id}` | Delete subject (and its attendance) | 200 / 404 |
| POST | `/attendance` | Mark attendance | 201 / 404 / 409 |
| GET | `/attendance/student/{studentId}` | Attendance of a student | 200 |
| GET | `/attendance/date/{yyyy-MM-dd}` | Attendance on a date | 200 |
| GET | `/attendance/percentage/student/{studentId}` | Overall percentage | 200 / 404 |
| GET | `/attendance/percentage/student/{studentId}/subject/{subjectId}` | Subject percentage | 200 / 404 |

### Sample requests (Postman body → raw JSON)

```json
POST /students
{ "name": "Asha Verma", "roll_no": "CSE101", "email": "asha@example.com", "branch": "CSE" }

POST /subjects
{ "name": "Data Structures", "code": "CS201" }

POST /attendance
{ "student_id": 1, "subject_id": 1, "attendance_date": "2026-09-29", "status": "present" }
```

`status` must be `present` or `absent` (case-insensitive).

Percentage response:
```json
{ "student_id": 1, "subject_id": 1, "attendance_percentage": 66.67 }
```

Error response:
```json
{ "message": "Attribute roll_no is missing or empty" }
```

## What changed from the Python version

| Python (Flask) | Java (Spring Boot) |
|---|---|
| `app.py` | `AttendanceApplication.java` + `application.properties` |
| `db.py` (mysql connector) | Spring Data JPA + HikariCP connection pool |
| `student.py`, `subject.py`, `attendance.py` (SQL) | `model/` entities + `repository/` interfaces + `service/` classes |
| `*_routes.py` | `controller/` classes |
| manual `required_fields` checks | `@Valid` + `@NotBlank` / `@NotNull` on DTO records |
| `.env` via python-dotenv | environment variables (`${DB_HOST:localhost}` in properties) |
| `test_api.py` | JUnit 5 tests in `src/test/java` |

Improvements included:
- Duplicate attendance (same student + subject + date) is blocked by both a service check **and** a database unique constraint, and now returns **409 Conflict** (previously 400).
- Marking attendance for a non-existent student/subject returns a clear **404**.
- Duplicate `roll_no`, `email` or subject `code` returns **409**.
- Deleting a student/subject also removes their attendance rows.
- Global exception handler gives consistent JSON errors (400 / 404 / 409 / 500).
- Emails are validated; status values are validated.

## Future enhancements
Spring Security + JWT roles, low-attendance alerts, pagination, CSV/PDF export, Swagger UI (springdoc-openapi), Dockerfile for the app.
