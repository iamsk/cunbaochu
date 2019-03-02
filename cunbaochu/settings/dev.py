from .common import *

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'test2',
    'USER': 'test',
    'PASSWORD': 'Dev@hfq',
    'HOST': '123.56.135.63',
    'PORT': '3306',
    'OPTIONS': {
    },
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "../static"),
)
