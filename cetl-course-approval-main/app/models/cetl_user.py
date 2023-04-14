from app.database import db
from .user import User

class CetlUser(User):
    __mapper_args__ = {
        "polymorphic_identity": "cetl",
    }

    def __init__(self, fullname, email, password):
        super().__init__(fullname, email, password)

    def __repr__(self):
        return f'<CetlUser {self.name}>'
