from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import *
from . import admin_blueprint
from app.database import db

@admin_blueprint.route("/queue", methods=["GET"])
def unassigned_queue():
    # Get all queues and render it in the queue page
    generic_queue = Queue.query.filter_by(owner_id=None).first()
    cetlUsers = CetlUser.query.all()
    if not generic_queue:
        generic_queue = Queue(None)
        db.session.add(generic_queue)
        db.session.commit()
    data = {
        'queue': generic_queue,
        'cetlUsers': cetlUsers
    }
    return render_template("admin/queue.html", **data )



@admin_blueprint.route("/queue", methods=["POST"])
def queue_assign_action():
    # Get all queues and render it in the queue page
    form_data = request.form
    submission_item = QueueItem.query.filter_by(submission_id=form_data['item_id']).first()

    cetl_user_queue = Queue.query.filter_by(owner_id=form_data['cetlUser']).first()
    if not cetl_user_queue:
        cetl_user_queue = Queue(form_data['cetlUser'])
        db.session.add(cetl_user_queue)
        db.session.commit()
    
    submission_item.queue_id = cetl_user_queue.id
    db.session.add(submission_item)
    db.session.commit()

    return redirect(url_for('admin.unassigned_queue'))


