from decouple import config
from os import environ
class Config:
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'SECRET_KEY': environ.get('SECRET_KEY'),
    'PGSQL_HOST': environ.get('PGSQL_HOST'),
    'PGSQL_USER': environ.get('PGSQL_USER'),
    'PGSQL_PASSWORD': environ.get('PGSQL_PASSWORD'),
    'PGSQL_DATABASE': environ.get('PGSQL_DATABASE')
}

