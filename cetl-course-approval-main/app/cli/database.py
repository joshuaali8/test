from flask.cli import AppGroup
from flask.cli import with_appcontext
from app.database import db
from app import models
import csv
import click

db_cli = AppGroup('database', help="Performs database initialization and loading")


@db_cli.command("init", help="Creates and initializes the database")
@with_appcontext
def initialize_db_cli():
    """This function is responsible for initializing the database. It would use the sqlalchemy database URI to connect
    to the database and it would create all the tables for the models that are defined in the models section of the
    application.
    This command can be executed as follows:
        - flask database init
    """

    db.create_all()
    db.session.commit()
    click.echo("Database Initialized successfully")


