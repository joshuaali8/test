from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import CetlUser, Lecturer, User

root_blueprint = Blueprint('root', __name__)

@root_blueprint.route("/", methods=["GET"])
def home_nav():
    # Return the correct page for the home page. Login if not authenticated or the relevant dashboard if authenticated
    if not current_user.is_authenticated:
        return redirect(url_for('login.login'))
    user_id = current_user.id
    
    cetl_user = CetlUser.query.filter_by(id=user_id).first()
    if cetl_user:
        return redirect(url_for('cetl.dashboard'))

    lecturer_user = Lecturer.query.filter_by(id=user_id).first()
    if lecturer_user:
        return redirect(url_for('lecturer.dashboard'))

    return redirect(url_for('admin.dashboard'))
