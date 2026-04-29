from flask import Blueprint, request, jsonify
from datetime import datetime
from services.groq_client import generate_response

describe_bp = Blueprint('describe', __name__)

def load_prompt():
    with open("prompts/describe_prompt.txt", "r") as f:
        return f.read()

@describe_bp.route('/', methods=['POST'])
def describe():
    data = request.json

    if not data or "title" not in data or "description" not in data:
        return jsonify({"error": "title and description are required"}), 400

    title = data["title"]
    description = data["description"]

    prompt_template = load_prompt()
    final_prompt = prompt_template.format(
        title=title,
        description=description
    )

    ai_output = generate_response(final_prompt)

    if not ai_output:
        return jsonify({"error": "AI service unavailable"}), 500

    return jsonify({
        "description": ai_output,
        "generated_at": datetime.utcnow().isoformat()
    })