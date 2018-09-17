import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wanguinjoka:hakiizzy@localhost/personalblog'

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wanguinjoka:hakiizzy@localhost/personalblog'
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}
