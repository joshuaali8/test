from flask import Blueprint, render_template, request, redirect, url_for, flash

cetl_blueprint = Blueprint('cetl', __name__, url_prefix="/cetl")

def register_blueprint(app):
    from . import dashboard
    from . import my_queue
    app.register_blueprint(cetl_blueprint)