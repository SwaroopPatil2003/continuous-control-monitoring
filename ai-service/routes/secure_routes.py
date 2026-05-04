from flask import Blueprint, request, jsonify
from services.sanitizer import sanitize_input

secure_bp = Blueprint("secure", __name__)

@secure_bp.route("/secure-input", methods=["POST"])
def secure_input():
    data = request.get_json()

    if not data or "input" not in data:
        return jsonify({"error": "Missing input field"}), 400

    result = sanitize_input(data["input"])

    if "error" in result:
        return jsonify(result), 400

    return jsonify({
        "message": "Input is safe",
        "clean_input": result["clean"]
    }), 200