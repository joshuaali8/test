from app.database import db
from .cetl_user import CetlUser
from .queue_item import QueueItem

class Queue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey(CetlUser.id), nullable=True)

    items = db.relationship(QueueItem, backref='queue')
    
    def __repr__(self):
        return f'<Queue {self.id}>'

    def __init__(self, owner_id):
        self.owner_id = owner_id