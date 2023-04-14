from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import *
from . import admin_blueprint
from app.database import db

@admin_blueprint.route("/lecturer", methods=["GET"])
def lecturer():
    # Get all lecturers and render it in the lecturer page
    all_lecturers = Lecturer.query.all()
    departments = Department.query.all()
    data = {
        'lecturers': all_lecturers,
        'departments': departments
    }
    return render_template("admin/lecturer.html", **data )

@admin_blueprint.route("/cetl_staff", methods=["GET"])
def cetl_staff():
    # Get all cetl_staffs and render it in the cetl_staff page
    all_cetl_staffs = CetlUser.query.all()
    data = {
        'cetl_staffs': all_cetl_staffs
    }
    return render_template("admin/cetl_staff.html", **data )

@admin_blueprint.route("/lecturer", methods=["POST"])
def lecturer_create_action():
    form_data = request.form
    full_name = form_data['full_name']
    email = form_data['email']
    password = form_data['password']
    department_id = form_data['department']

    new_lecturer = Lecturer(full_name, email, password, department_id)
    db.session.add(new_lecturer)
    db.session.commit()

    return redirect(url_for('admin.lecturer'))


@admin_blueprint.route("/cetl_staff", methods=["POST"])
def cetluser_create_action():
    form_data = request.form
    full_name = form_data['full_name']
    email = form_data['email']
    password = form_data['password']

    new_cetl_user = CetlUser(full_name, email, password)
    db.session.add(new_cetl_user)
    db.session.commit()

    # When a CETL user is created, create a Queue for that user as well
    new_queue = Queue(new_cetl_user.id)
    db.session.add(new_queue)
    db.session.commit()

    return redirect(url_for('admin.cetl_staff'))