from flask import Blueprint, render_template, request, redirect, url_for, flash

lecturer_blueprint = Blueprint('lecturer', __name__, url_prefix="/lecturer")

def register_blueprint(app):
    from . import dashboard
    from . import course_outline
    from . import programme_outline
    from . import course_submission
    app.register_blueprint(lecturer_blueprint)