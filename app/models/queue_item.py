from app.database import db
from .course_submission import CourseSubmission

class QueueItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    submission_id = db.Column(db.Integer, db.ForeignKey(CourseSubmission.id), nullable=False)
    queue_id = db.Column(db.Integer, db.ForeignKey('queue.id'), nullable=False)
    sequence = db.Column(db.Integer, nullable=False)
    
    submission = db.relationship(CourseSubmission,)
    
    def __repr__(self):
        return f'<QueueItem {self.id}>'

    def __init__(self, submission_id, sequence):
        self.submission_id = submission_id
        self.sequence = sequence