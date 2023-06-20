import os


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Config(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    TESTING = True
