from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, send_from_directory, send_file, jsonify, current_app
from flask_login import current_user, login_user, logout_user
from app.models import CetlUser, Lecturer, User, Course, CourseSubmission, CourseSubmissionVersion, Queue, QueueItem
from . import lecturer_blueprint
from course_docx_generator.App.maker import writeDoc
from app.database import db
from werkzeug.utils import secure_filename
import os
from datetime import datetime

@lecturer_blueprint.route("/course-outline", methods=["GET"])
def course_outline():
    all_courses = Course.query.all()
    lecturer = current_user
    submissions = lecturer.course_submissions

    data = {
        'submissions': submissions,
        'courses': all_courses
    }
    return render_template("lecturer/course-outline.html", **data)

@lecturer_blueprint.route("/course-outline", methods=["POST"])
def course_outline_action():
    form_data = request.form
    course_id = form_data['course']
    document = request.files['document']
    version = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    filename = f"{version}--{secure_filename(document.filename)}"
    document.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    # Create the submisison
    new_submission = CourseSubmission(course_id, current_user.id)
    db.session.add(new_submission)
    db.session.commit()

    # Create the version
    submission_version = CourseSubmissionVersion(new_submission.id, version, filename)
    db.session.add(submission_version)
    db.session.commit()

    #Add the submission to the unassigned queue
    generic_queue = Queue.query.filter_by(owner_id=None).first()
    if not generic_queue:
        generic_queue = Queue(None)
        db.session.add(generic_queue)
        db.session.commit()
    
    generic_queue.items.append(QueueItem(new_submission.id, len(generic_queue.items)))
    db.session.add(generic_queue)
    db.session.commit()
    
    return redirect(url_for('lecturer.course_outline'))


@lecturer_blueprint.route("/generate-course-outline", methods=["GET"])
def generate_course_outline():
    return render_template("lecturer/generate-course-outline.html")

@lecturer_blueprint.route("/generate-course-outline", methods=["POST"])
def generate_course_outline_action():
    json_data = request.json
    filename = writeDoc(json_data)
    return jsonify({
        'filename': filename
    })

@lecturer_blueprint.route("/generate-course-outline/download/<filename>", methods=["GET"])
def lecturer_download_file(filename):
    return send_from_directory(directory=current_app.instance_path, path=filename, as_attachment=True)


