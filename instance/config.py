class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '<super secret hey>'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db' # 'postgresql://<username>:<password>@<postgres_host>:<postgres_port>/<db_name>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_TOKEN_LOCATION = ["headers", "cookies"]
    JWT_COOKIE_CSRF_PROTECT = True


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    JWT_COOKIE_CSRF_PROTECT = False


class TestingConfig(Config):
    TESTING = True