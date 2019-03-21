from .common import *
import dj_database_url

db_from_env = dj_database_url.config(env='DATABASE_URL', conn_max_age=5000)

DATABASES['default'].update(db_from_env)
ALLOWED_HOSTS = ['*']
DEBUG = False
