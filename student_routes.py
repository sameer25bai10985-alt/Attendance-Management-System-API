from flask import Blueprint, jsonify, request

from models.student import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student,
    search_students
)


student_bp = Blueprint("student_bp", __name__)


# Create Student
@student_bp.route("/students", methods=["POST"])
def create_student_route():

    data = request.get_json()

    if data is None:
        return jsonify({
            "message": "Request must be JSON"
        }), 400

    required_fields = ["name", "roll_no", "email", "branch"]

    for field in required_fields:

        if field not in data:
            return jsonify({
                "message": f"Attribute {field} missing"
            }), 400

        if not str(data[field]).strip():
            return jsonify({
                "message": f"Attribute {field} cannot be empty"
            }), 400

    saved = create_student(data)

    if not saved:
        return jsonify({
            "message": "Failed to save student"
        }), 500

    return jsonify({
        "message": "Student saved successfully",
        "data": data
    }), 201


# Get All Students
@student_bp.route("/students", methods=["GET"])
def get_all_students_route():

    students = get_all_students()

    if students is None:
        return jsonify({
            "message": "Failed to fetch students"
        }), 500

    return jsonify({
        "data": students
    }), 200


# Get Student by ID
@student_bp.route("/students/<int:student_id>", methods=["GET"])
def get_student_by_id_route(student_id):

    student = get_student_by_id(student_id)

    if student is None:
        return jsonify({
            "message": "Student not found"
        }), 404

    return jsonify({
        "data": student
    }), 200


# Update Student
@student_bp.route("/students/<int:student_id>", methods=["PUT"])
def update_student_route(student_id):

    data = request.get_json()

    if data is None:
        return jsonify({
            "message": "Request must be JSON"
        }), 400

    required_fields = ["name", "roll_no", "email", "branch"]

    for field in required_fields:

        if field not in data:
            return jsonify({
                "message": f"Attribute {field} missing"
            }), 400

        if not str(data[field]).strip():
            return jsonify({
                "message": f"Attribute {field} cannot be empty"
            }), 400

    updated = update_student(student_id, data)

    if not updated:
        return jsonify({
            "message": "Student not found or update failed"
        }), 404

    return jsonify({
        "message": "Student updated successfully",
        "data": data
    }), 200


# Delete Student
@student_bp.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student_route(student_id):

    deleted = delete_student(student_id)

    if not deleted:
        return jsonify({
            "message": "Student not found"
        }), 404

    return jsonify({
        "message": "Student deleted successfully"
    }), 200


# Search Student
@student_bp.route("/students/search", methods=["GET"])
def search_students_route():

    keyword = request.args.get("keyword")

    if not keyword:
        return jsonify({
            "message": "Keyword is required"
        }), 400

    students = search_students(keyword)

    if students is None:
        return jsonify({
            "message": "Failed to search students"
        }), 500

    return jsonify({
        "data": students
    }), 200
