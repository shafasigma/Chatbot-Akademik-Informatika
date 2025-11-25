import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DB_HOST = os.environ.get("MYSQLHOST")
DB_USER = os.environ.get("MYSQLUSER")
DB_PASS = os.environ.get("MYSQLPASSWORD")
DB_NAME = os.environ.get("MYSQLDATABASE")
DB_PORT = os.environ.get("MYSQLPORT", 3306)

if DB_HOST and DB_USER and DB_PASS and DB_NAME:
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    print("====== USING RAILWAY MYSQL ======")
else:
    # fallback lokal
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:@localhost/chatbot_db"
    print("====== USING LOCAL MYSQL ======")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "supersecret"

db = SQLAlchemy(app)
