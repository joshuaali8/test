from flask import Blueprint, render_template, request, redirect, url_for, flash

admin_blueprint = Blueprint('admin', __name__)

def register_blueprint(app):
    from . import dashboard
    from . import user
    from . import faculty
    from . import department
    from . import programme
    from . import course
    from . import resource
    from . import queue
    app.register_blueprint(admin_blueprint)