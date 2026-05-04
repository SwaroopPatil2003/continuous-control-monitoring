from flask import Flask, jsonify
from routes.secure_routes import secure_bp

app = Flask(__name__)

# ✅ Register blueprint
app.register_blueprint(secure_bp)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "AI service running"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)