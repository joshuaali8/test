from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import *
from . import admin_blueprint
from app.database import db

@admin_blueprint.route("/department", methods=["GET"])
def department():
    # Get all departments and render it in the department page
    departments = Department.query.all()
    faculties = Faculty.query.all()
    data = {
        'departments': departments,
        'faculties': faculties
    }
    return render_template("admin/department.html", **data )



@admin_blueprint.route("/department", methods=["POST"])
def department_create_action():
    # Get all departments and render it in the department page
    form_data = request.form
    name = form_data['department']
    faculty_id = form_data['faculty']

    new_department = Department(name, faculty_id)
    db.session.add(new_department)
    db.session.commit()
    return redirect(url_for('admin.department'))


