from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# JWT setup
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET", "super-secret-key")
jwt = JWTManager(app)

# Import blueprints AFTER app setup
from routes.auth import auth_bp
from routes.tasks import tasks_bp
from routes.completions import completions_bp
from routes.leaderboard import leaderboard_bp

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(tasks_bp, url_prefix="/tasks")
app.register_blueprint(completions_bp, url_prefix="/completions")
app.register_blueprint(leaderboard_bp, url_prefix="/leaderboard")

if __name__ == "__main__":
    app.run(debug=True)
