from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = 'a9xcbii$8bx!k3krtg+92v2vt5o+=l14b2)bda-#1_tr)(2%9)'

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'south',
    'social.apps.django_app.default',
)

LOCAL_APPS = (
    'apps.home',
    'apps.users',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SistemaDiscusiones.urls'

WSGI_APPLICATION = 'SistemaDiscusiones.wsgi.application'

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
        'social.backends.facebook.FacebookAppOAuth2',
        'social.backends.facebook.FacebookOAuth2',
        'social.backends.twitter.TwitterOAuth',
        'django.contrib.auth.backends.ModelBackend',
    )   

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/error/'

SOCIAL_AUTH_USER_MODEL = 'apps.User'