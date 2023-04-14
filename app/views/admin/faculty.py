from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import *
from . import admin_blueprint
from app.database import db

@admin_blueprint.route("/faculty", methods=["GET"])
def faculty():
    # Get all facultys and render it in the faculty page
    all_faculties = Faculty.query.all()
    data = {
        'all_faculties': all_faculties,
    }
    return render_template("admin/faculty.html", **data )



@admin_blueprint.route("/faculty", methods=["POST"])
def faculty_create_action():
    # Get all facultys and render it in the faculty page
    form_data = request.form
    name = form_data['faculty']

    new_faculty = Faculty(name)    
    db.session.add(new_faculty)
    db.session.commit()
    return redirect(url_for('admin.faculty'))


