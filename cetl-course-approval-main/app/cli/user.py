from flask.cli import AppGroup
from flask.cli import with_appcontext
from app.database import db
from app.models import *
import csv
import click

user_cli = AppGroup('user', help="Performs database initialization and loading")


@user_cli.command("create-admin", help="Creates and initializes the database")
@with_appcontext
def create_user():
    fullname = click.prompt('Enter the full name of the user', default="John Doe")
    email = click.prompt('Enter the email of the user', default="user@sta.uwi.edu")
    password = click.prompt('Please enter a password for the user', default="password")
    
    user = User(fullname, email, password)
    db.session.add(user)
    db.session.commit()
    click.echo("Admin user created successfully")

