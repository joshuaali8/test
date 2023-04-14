from app.database import db

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    detail = db.Column(db.String, nullable=False)

    def __init__(self, title, detail):
        self.title = title
        self.detail = detail

    def __repr__(self):
        return f'<Resource {self.name}>'
