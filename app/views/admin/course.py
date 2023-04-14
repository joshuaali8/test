from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import *
from . import admin_blueprint
from app.database import db

@admin_blueprint.route("/course", methods=["GET"])
def course():
    # Get all courses and render it in the course page
    all_courses = Course.query.all()
    all_programmes = Programme.query.all()
    data = {
        'all_courses': all_courses,
        'programmes': all_programmes
    }
    return render_template("admin/course.html", **data )



@admin_blueprint.route("/course", methods=["POST"])
def course_create_action():
    # Get all courses and render it in the course page
    form_data = request.form
    code = form_data['code']
    name = form_data['course']
    programmes = form_data.getlist('programme')

    new_course = Course(name, code)
    db.session.add(new_course)
    db.session.commit()

    for programme in programmes:
        course_programme = Programme.query.get(programme)
        new_course.programmes.append(course_programme)
    
    db.session.add(new_course)
    db.session.commit()
    return redirect(url_for('admin.course'))


