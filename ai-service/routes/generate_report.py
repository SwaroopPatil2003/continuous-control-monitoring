from flask import Blueprint, jsonify
from services.limiter import limiter

generate_bp = Blueprint("generate", __name__)

@generate_bp.route("/generate-report", methods=["POST"])
@limiter.limit("10 per minute")
def generate_report():
    return jsonify({
        "message": "Report generated (placeholder)"
    })