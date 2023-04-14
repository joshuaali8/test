from werkzeug.security import check_password_hash, generate_password_hash
from app.database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)

    # Setting this up for single table inheritance for Superadmins, Lecturers and CETL Staff
    __mapper_args__ = {
        "polymorphic_identity": "superadmin",
        "polymorphic_on": user_type,
    }


    def __init__(self, fullname, email, password):
        self.full_name = fullname
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')


    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)