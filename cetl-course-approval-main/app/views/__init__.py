from . import common
from . import admin
from . import cetl
from . import lecturer

def init_app(app):
    common.register_blueprint(app)
    admin.register_blueprint(app)
    cetl.register_blueprint(app)
    lecturer.register_blueprint(app)