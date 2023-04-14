from app.database import db
from datetime import datetime
from .user import User
from .course_submission_version import CourseSubmissionVersion

class CourseSubmissionVersionComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    version_id = db.Column(db.Integer, db.ForeignKey(CourseSubmissionVersion.id), nullable=False)
    commenter_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    comment = db.Column(db.String, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, version_id,commenter_id,comment):
        self.version_id = version_id
        self.commenter_id = commenter_id
        self.comment = comment

    def __repr__(self):
        return f'<CourseSubmissionVersionComment {self.id}>'
