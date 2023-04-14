from app.database import db
from .programme import Programme

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)

    programmes = db.relationship(Programme, secondary='programme_course', backref="courses")


    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return f'<Course {self.name}>'
