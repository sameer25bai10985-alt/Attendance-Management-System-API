# Design Decisions & Rationale

1. Flask Blueprints over a  the single monolithic file
Each resource (subjects, students, attendance) has its own `Blueprint` in `routes`. This keeps
route definitions small makes it easy to see which endpoints belong to which resource and
 the lets each blueprint be registered independently in `app.py`.

2. Separating routes from models
Routes only handle HTTP concerns: parsing the request, validating required fields, and shaping
the JSON response with the right status code. All SQL lives in `models`. This means the data
layer can be tested or reused  without going through Flask at all.

 3. Database-level uniqueness instead of application-level checks only
Duplicate attendance prevention is enforced with a `UNIQUE(student_id, subject_id,
attendance_date)` constraint in MySQL not just an application-side check. This guarantees
correctness even under concurrent requests where two near-simultaneous API calls could both
pass an application-level "does this exist?" check before either has written its row.

4. Credentials via environment variables
`db.py` originally had a hardcoded database password. This was changed to read
`DB_HOST` / `DB_USER` / `DB_PASSWORD` / `DB_NAME` from the environment (with `localhost`/`root`
as safe local defaults), so real credentials never need to be committed to source control.

5. Plain integer foreign keys instead of enforced FK constraints (for now)
`attendance.student_id` and `attendance.subject_id` are integers that logically reference
`students.id` and `subjects.id`, but are not yet declared with `FOREIGN KEY` constraints. This
was a scope decision to keep the initial schema simple; adding the constraints is listed under
Future Enhancements.

## 6. REST + JSON over a templated/HTML frontend
The project is scoped as a backend API so it can be consumed by any future frontend (web,
mobile, or another service) rather than tying the logic to the specific UI.
