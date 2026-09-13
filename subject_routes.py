from flask import Blueprint, jsonify, request

from models.subject import (
    create_subject,
    get_all_subjects,
    get_subject_by_id,
    update_subject,
    delete_subject
)


subject_bp = Blueprint("subject_bp", __name__)


# Create Subject
@subject_bp.route("/subjects", methods=["POST"])
def create_subjects_route():

    data = request.get_json()

    if data is None:
        return jsonify({
            "message": "Request must be JSON"
        }), 400

    required_fields = ["name", "code"]

    for field in required_fields:

        if field not in data:
            return jsonify({
                "message": f"Attribute {field} missing"
            }), 400

        if not str(data[field]).strip():
            return jsonify({
                "message": f"Attribute {field} cannot be empty"
            }), 400

    saved = create_subject(data)

    if not saved:
        return jsonify({
            "message": "Failed to save subject"
        }), 500

    return jsonify({
        "message": "Successfully saved subject",
        "data": data
    }), 201


# Get All Subjects
@subject_bp.route("/subjects", methods=["GET"])
def get_all_subjects_route():

    subjects = get_all_subjects()

    if subjects is None:
        return jsonify({
            "message": "Failed to fetch subjects"
        }), 500

    return jsonify({
        "data": subjects
    }), 200


# Get Subject by ID
@subject_bp.route("/subjects/<int:subject_id>", methods=["GET"])
def get_subject_by_id_route(subject_id):

    subject = get_subject_by_id(subject_id)

    if subject is None:
        return jsonify({
            "message": "Subject not found"
        }), 404

    return jsonify({
        "data": subject
    }), 200


# Update Subject
@subject_bp.route("/subjects/<int:subject_id>", methods=["PUT"])
def update_subject_route(subject_id):

    data = request.get_json()

    if data is None:
        return jsonify({
            "message": "Request must be JSON"
        }), 400

    required_fields = ["name", "code"]

    for field in required_fields:

        if field not in data:
            return jsonify({
                "message": f"Attribute {field} missing"
            }), 400

        if not str(data[field]).strip():
            return jsonify({
                "message": f"Attribute {field} cannot be empty"
            }), 400

    updated = update_subject(subject_id, data)

    if not updated:
        return jsonify({
            "message": "Subject not found or update failed"
        }), 404

    return jsonify({
        "message": "Subject updated successfully",
        "data": data
    }), 200


# Delete Subject
@subject_bp.route("/subjects/<int:subject_id>", methods=["DELETE"])
def delete_subject_route(subject_id):

    deleted = delete_subject(subject_id)

    if not deleted:
        return jsonify({
            "message": "Subject not found"
        }), 404

    return jsonify({
        "message": "Subject deleted successfully"
    }), 200
