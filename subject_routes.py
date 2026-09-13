from flask import Blueprint,jsonify,request
from models.subject import create_subject, get_all_subjects

attendance_bp=Blueprint("attendance_bp",__name__)

@attendance_bp.route("/subjects", methods=["POST"])
def create_subjects_route():
    data = request.get_json()

    if data is None:
      return jsonify({"message":"Request must be json"}) ,400

    required_fields=["name","code"]

    for field in required_fields:
        if field not in data:
            return jsonify({"message":f"attribute {field} missing "}),400

        if not str(data[field]).strip():
            return jsonify({"message":f"attribute {field} cannot be empty"}),400

    saved = create_subject(data)

    if not saved:
        return jsonify({"message":"Failed to Save Subject"}),500
    return jsonify({
        "message":"Successfully Save Subject",
        "data":data
    }),201

@attendance_bp.route("/subjects", methods=["GET"])
def get_all_subjects_route():
    subject = get_all_subjects()

    if subject is None:
        return jsonify({"message":"Failed to Fetch Subject"}),500

    return jsonify({
        "data":subject
    }),200
