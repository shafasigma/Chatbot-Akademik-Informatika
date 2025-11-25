import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ===========================
# 🔧 CONFIG MYSQL RAILWAY
# ===========================
MYSQL_URL = os.environ.get("MYSQL_URL")

if MYSQL_URL:
    # Jika Railway memberi "mysql://", ubah jadi "mysql+pymysql://"
    if MYSQL_URL.startswith("mysql://"):
        MYSQL_URL = MYSQL_URL.replace("mysql://", "mysql+pymysql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = MYSQL_URL
else:
    # ===========================
    # 🔧 CONFIG LOCAL FALLBACK
    # ===========================
    DB_USER = "root"
    DB_PASS = ""
    DB_HOST = "localhost"
    DB_NAME = "chatbot_db"

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    )

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "supersecret"

db = SQLAlchemy(app)

# ===========================
# 🔧 PATH DIRECTORIES
# ===========================
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")
UPLOADS_DIR = os.path.join(BASE_DIR, "uploads")

os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(os.path.join(UPLOADS_DIR, "datasets"), exist_ok=True)
os.makedirs(os.path.join(UPLOADS_DIR, "pdfs"), exist_ok=True)
