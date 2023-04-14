from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import *
from . import admin_blueprint
from app.database import db

@admin_blueprint.route("/programme", methods=["GET"])
def programme():
    # Get all programmes and render it in the programme page
    all_programmes = Programme.query.all()
    all_departments = Department.query.all()
    data = {
        'all_programmes': all_programmes,
        'departments': all_departments
    }
    return render_template("admin/programme.html", **data )



@admin_blueprint.route("/programme", methods=["POST"])
def programme_create_action():
    # Get all programmes and render it in the programme page
    form_data = request.form
    name = form_data['programme']
    department_id = form_data['department']

    new_programme = Programme(name, department_id)  
    db.session.add(new_programme)
    db.session.commit()
    return redirect(url_for('admin.programme'))


