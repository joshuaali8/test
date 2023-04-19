from werkzeug.security import check_password_hash, generate_password_hash
from app.database import db
from datetime import datetime

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, nullable=False)
    recipient_id = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(4096), nullable=False)

