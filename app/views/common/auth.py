from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import CetlUser, Lecturer, User

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@login_blueprint.route("/login", methods=["POST"])
def login_action():
    form_data = request.form
    email = form_data['email']
    password = form_data['password']

    if email and password:
        # Check if the user is a CETL user
        cetl_user = CetlUser.query.filter_by(email=email).first()
        if cetl_user and cetl_user.check_password(password):
            login_user(cetl_user)
            return redirect(url_for('cetl.dashboard'))
        
        # Check if the user is a lecturer
        lecturer = Lecturer.query.filter_by(email=email).first()
        if lecturer and lecturer.check_password(password):
            login_user(lecturer)
            return redirect(url_for('lecturer.dashboard'))
            
        # Check to see if the user is a superadmin
        admin = User.query.filter_by(email=email).first()
        if admin and admin.check_password(password):
            login_user(admin)
            return redirect(url_for('admin.dashboard'))

    flash("Invalid credentials. Please try again")
    return render_template("login.html")


@login_blueprint.route("/logout", methods=["GET","POST"])
def logout_action():
    logout_user()
    return redirect(url_for('login.login'))