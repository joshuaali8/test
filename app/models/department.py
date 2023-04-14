from app.database import db
from .faculty import Faculty

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey(Faculty.id), nullable=False)

    def __init__(self, name, faculty_id):
        self.name = name
        self.faculty_id = faculty_id

    def __repr__(self):
        return f'<Department {self.name}>'
