"""CLI
The CLI module contains all the custom commands that can be run in the terminal.
These commands provide functionality that may be required to set up the application initially or perform
testing from the command line interface rather than the user interface.
"""

from .database import db_cli
from .user import user_cli

def init_app(app):
    """This function is a function that registers the commands for the CLI.
    All of these functions can be called using the command that's specified in the click command function decorator.
    The usual format of the commands are as follows:
        flask <command>
    """
    app.cli.add_command(db_cli)
    app.cli.add_command(user_cli)