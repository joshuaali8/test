from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import *
from . import admin_blueprint
from app.database import db

@admin_blueprint.route("/resource", methods=["GET"])
def resource():
    # Get all resources and render it in the resource page
    all_resources = Resource.query.all()
    data = {
        'all_resources': all_resources,
    }
    return render_template("admin/resource.html", **data )



@admin_blueprint.route("/resource", methods=["POST"])
def resource_create_action():
    # Get all resources and render it in the resource page
    form_data = request.form
    title = form_data['title']
    detail = form_data['detail']

    new_resource = Resource(title, detail)    
    db.session.add(new_resource)
    db.session.commit()
    return redirect(url_for('admin.resource'))


