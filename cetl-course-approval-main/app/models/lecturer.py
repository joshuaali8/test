from app.database import db
from .user import User
from .department import Department

class Lecturer(User):
    department_id = db.Column(db.Integer, db.ForeignKey(Department.id), nullable=True)

    department = db.relationship(Department, backref='lecturers')
    
    __mapper_args__ = {
        "polymorphic_identity": "lecturer",
    }

    def __init__(self, fullname, email, password, department_id):
        super().__init__(fullname, email, password)
        self.department_id = department_id


    def __repr__(self):
        return f'<Lecturer {self.name}>'
