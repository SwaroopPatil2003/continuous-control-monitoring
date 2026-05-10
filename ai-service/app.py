from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from routes.secure_routes import secure_bp
from routes.generate_report import generate_bp



app = Flask(__name__)
from flask_talisman import Talisman
Talisman(app)


limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)


app.register_blueprint(secure_bp)
app.register_blueprint(generate_bp)




app.view_functions['generate.generate_report'] = limiter.limit("10 per minute")(
    app.view_functions['generate.generate_report']
)


@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({
        "error": "Too many requests",
        "retry_after": str(e.description)
    }), 429


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "AI service running"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)