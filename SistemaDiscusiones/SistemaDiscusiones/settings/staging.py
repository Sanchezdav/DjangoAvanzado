from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Discusiones',
        'USER': 'David',
        'PASSWORD': '8608',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY = '1424631281119857'
SOCIAL_AUTH_FACEBOOK_SECRET = '7019b4d6f923afc401c82d2256d96108'

SOCIAL_AUTH_TWITTER_KEY = 'HJmSIaoX60DBEo9KVa1m1vJ7x'
SOCIAL_AUTH_TWITTER_SECRET = 'gb1f66q0hKK45UWUGY0hanlRt4DG82iE2myQGEZcgHyoxxWrLA'

MANDRILL_API_KEY = 'VHK0CZY3VL57PUJMh_0rGw'

CACHES = {
	'default' : {
		'BACKEND' : 'redis_cache.RedisCache',
		#'LOCATION' : redistogo
		'LOCATION' : 'localhost:6379',
		'OPTIONS' : {
			'DB' : 1,
			#'PASSWORD' :
		}
	}
}