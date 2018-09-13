import os


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vikki:sasawa@localhost/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    pass


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
