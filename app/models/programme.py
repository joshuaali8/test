from app.database import db
from .department import Department


class Programme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey(Department.id), nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)

    department = db.relationship(Department, backref='programmes')


    def __init__(self, name, department_id):
        self.name = name
        self.department_id = department_id

    def __repr__(self):
        return f'<Programme {self.name}>'
