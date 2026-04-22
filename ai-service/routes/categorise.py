from flask import Blueprint, request, jsonify
from services.groq_client import GroqClient
import json
import re

categorise_bp = Blueprint("categorise", __name__)

client = GroqClient()

@categorise_bp.route("/categorise", methods=["POST"])
def categorise():
    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({"error": "Please provide 'text' in JSON body"}), 400

        user_text = data["text"].strip()

        if not user_text:
            return jsonify({"error": "Text cannot be empty"}), 400

        prompt = f"""
You are a classification AI.

Classify the following text into ONE of these categories only:

Security
Performance

Return ONLY valid JSON in this format:
{{
  "category": "CategoryName",
  "confidence": 0.95,
  "reasoning": "Short reason"
}}

Text:
{user_text}
"""

        response = client.generate_text(prompt)

        match = re.search(r'\{.*\}', response, re.DOTALL)

        if not match:
            return jsonify({
                "category": "General",
                "confidence": 0.50,
                "reasoning": "Could not parse AI response"
            })

        result = json.loads(match.group())

        return jsonify(result)

    except Exception as error:
        return jsonify({
            "category": "General",
            "confidence": 0.0,
            "reasoning": str(error)
        }), 500