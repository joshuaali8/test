from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import CetlUser, Lecturer, User
from . import lecturer_blueprint

@lecturer_blueprint.route("/chat", methods=["GET"])
def cetl_staff():
    # Get all cetl_staffs and render it in the cetl_staff page
    all_cetl_staffs = CetlUser.query.all()
    data = {
        'cetl_staffs': all_cetl_staffs
    }
    return render_template("lecturer/chat.html", **data )

