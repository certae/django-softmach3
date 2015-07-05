import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'db.sqlite3'),
    }
}



DEBUG = True



# add email settings
HOST_DOMAIN = '127.0.0.1:8000'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'certae.sm@gmail.com'
EMAIL_HOST_PASSWORD = 'dariogomezt'
DEFAULT_FROM_EMAIL = 'certae.sm@gmail.com'

# used for debug
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

FIXTURE_DIRS = ( os.path.join(BASE_DIR, 'fixtures'),  )
