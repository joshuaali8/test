from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import CetlUser, Lecturer, User
from . import lecturer_blueprint

@lecturer_blueprint.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("lecturer/dashboard.html")
