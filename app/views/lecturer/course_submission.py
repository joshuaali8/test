from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, send_from_directory, send_file, jsonify, current_app
from flask_login import current_user, login_user, logout_user
from app.models import CetlUser, Lecturer, User, Course, CourseSubmission, CourseSubmissionVersion
from . import lecturer_blueprint
#from course_docx_generator.App.maker import writeDoc
from app.database import db
from werkzeug.utils import secure_filename
import os
from datetime import datetime

@lecturer_blueprint.route("/course-submission/<int:submission_id>", methods=["GET"])
def course_submission(submission_id):
    submission = CourseSubmission.query.get(submission_id)

    data = {
        'submission': submission
    }
    return render_template("lecturer/course-submission.html", **data)

@lecturer_blueprint.route("/course-submission/<int:submission_id>", methods=["POST"])
def course_submission_action(submission_id):
    form_data = request.form
    document = request.files['document']
    version = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    filename = f"{version}--{secure_filename(document.filename)}"
    document.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    # Create the version
    submission_version = CourseSubmissionVersion(submission_id, version, filename)
    db.session.add(submission_version)
    db.session.commit()

    return redirect(url_for('lecturer.course_submission', submission_id=submission_id))

