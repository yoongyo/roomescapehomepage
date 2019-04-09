from .common import *

ALLOWED_HOSTS = ['*']
DEBUG = False


AWS_ACCESS_KEY_ID = 'AKIAVNC3EVGMGNL5BLSR'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'bucheonroute'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'mysite/static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'