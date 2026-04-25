from flask import Blueprint, request, jsonify

describe_bp = Blueprint('describe', __name__)

def load_prompt():
    with open("prompts/describe_prompt.txt", "r") as f:
        return f.read()

@describe_bp.route('/', methods=['POST'])
def describe():
    data = request.json

    title = data.get("title", "")
    description = data.get("description", "")

    prompt_template = load_prompt()

    final_prompt = prompt_template.format(
        title=title,
        description=description
    )

    return jsonify({
        "generated_prompt": final_prompt
    })