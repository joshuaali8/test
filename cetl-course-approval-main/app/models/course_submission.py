from app.database import db
from .course import Course
from .lecturer import Lecturer

class CourseSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey(Course.id), nullable=False)
    lecturer_id = db.Column(db.Integer, db.ForeignKey(Lecturer.id), nullable=False)
    status = db.Column(db.String, default="Pending")

    course = db.relationship(Course, backref='submissions')
    lecturer = db.relationship(Lecturer, backref="course_submissions")


    def __init__(self, course_id, lecturer_id):
        self.course_id = course_id
        self.lecturer_id = lecturer_id

    def __repr__(self):
        return f'<CourseSubmission {self.id}>'
