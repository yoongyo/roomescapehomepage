from .common import *
import dj_dtatebase_url

db_from_env = dj_dtatebase_url.config(env='DATABASE_URL', conn_max_age=5000)

DATABASES['default'].update(db_from_env)
ALLOWED_HOSTS = ['https://roomescape1.herokuapp.com', 'roomescape1.herokuapp.com']
DEBUG = False
