from flask import Flask

from routes.subject_routes import subject_bp
from routes.attendance_routes import attendance_bp
from routes.student_routes import student_bp


app = Flask(__name__)

app.register_blueprint(subject_bp)
app.register_blueprint(attendance_bp)
app.register_blueprint(student_bp)


if __name__ == '__main__':
    app.run(debug=True)
