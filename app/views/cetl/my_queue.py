from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import CetlUser, Lecturer, User, Queue
from . import cetl_blueprint
from app.database import db

@cetl_blueprint.route("/my-queue", methods=["GET"])
def my_queue():
    personal_queue = Queue.query.filter_by(owner_id=current_user.id).first()
    if not personal_queue:
        personal_queue = Queue(current_user.id)
        db.session.add(personal_queue)
        db.session.commit()

    data = {
        'queue': personal_queue
    }

    return render_template("cetl/queue.html", **data)
