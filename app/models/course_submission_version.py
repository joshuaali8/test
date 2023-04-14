from app.database import db
from datetime import datetime
from .course_submission import CourseSubmission

class CourseSubmissionVersion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String, nullable=False)
    submission_id = db.Column(db.Integer, db.ForeignKey(CourseSubmission.id), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now())
    filename = db.Column(db.String, nullable=False)
    
    submission = db.relationship(CourseSubmission, backref='versions')


    def __init__(self, submission_id, version, filename):
        self.submission_id = submission_id
        self.version = version
        self.filename = filename

    def __repr__(self):
        return f'<CourseSubmissionVersion {self.id}>'
