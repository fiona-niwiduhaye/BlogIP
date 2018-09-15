import os


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # configure the path to where image files will be saved since it is not advisable to save files in the database
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
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
