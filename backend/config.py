import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

# Ambil database dari Railway
DATABASE_URL = os.environ.get("DATABASE_URL")

# Perbaiki driver jika Railway memberikan mysql:// tanpa driver
if DATABASE_URL and DATABASE_URL.startswith("mysql://"):
    DATABASE_URL = DATABASE_URL.replace("mysql://", "mysql+pymysql://")

if DATABASE_URL:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
else:
    # Fallback lokal
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:@localhost/chatbot_db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "supersecret"

db = SQLAlchemy(app)

# folder-folde
MODEL_DIR = os.path.join(BASE_DIR, "model")
UPLOADS_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(os.path.join(UPLOADS_DIR, "datasets"), exist_ok=True)
os.makedirs(os.path.join(UPLOADS_DIR, "pdfs"), exist_ok=True)
