from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import auth
from . import root

def register_blueprint(app):
    app.register_blueprint(auth.login_blueprint)
    app.register_blueprint(root.root_blueprint)
