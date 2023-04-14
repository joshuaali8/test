from app.database import db
from .programme import Programme
from .course import Course


programme_courses_m2m = db.Table(
    "programme_course",
    db.Column("programme_id", db.ForeignKey(Programme.id), primary_key=True),
    db.Column("course_id", db.ForeignKey(Course.id), primary_key=True),
)