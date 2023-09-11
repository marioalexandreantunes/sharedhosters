from pathlib import Path

# mario ANTUNES 2023 - adicionado
from decouple import config
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# mario ANTUNES 2023 - adicionado
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# mario ANTUNES 2023 - adicionado
DEBUG = config('DEBUG', default=True, cast=bool)

# mario ANTUNES 2023 - adicionado
ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(" ")

# mario ANTUNES 2023 - adicionado
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS').split(" ")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # mario ANTUNES 2023 - adicionado
    'admin_honeypot',
    'cloudinary',
]

MIDDLEWARE = [
    # mario ANTUNES 2023 - adicionado
    # https://www.geeksforgeeks.org/adding-csp-headers-in-django-project/
    'csp.middleware.CSPMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

USE_MYSQL = False

# mario ANTUNES 2023 - adicionado
if USE_MYSQL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASS'),
            'HOST':config('DB_HOST'),
            'PORT':config('DB_PORT'),
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            }
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# mario ANTUNES 2023 - adicionado
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]

if not DEBUG:
    # Verifica no CPanel onde está a pasta 'public' para o teu dominio
    STATIC_ROOT = '/home/USERNAME/public_html/static'
    # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ADD --MA-- Algumas opções para segurança em produção
# https://www.freecodecamp.org/news/how-to-build-a-secure-django-web-app/
# https://learndjango.com/tutorials/django-best-practices-security
# https://vegibit.com/how-to-secure-your-django-application-and-protect-user-data/
# https://dev.to/thepylot/django-web-security-checklist-before-deployment-secure-your-django-app-4jb8
# https://docs.djangoproject.com/en/4.2/topics/security/
if not DEBUG:
    X_FRAME_OPTIONS = 'DENY'
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 15768000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    # SECURE_SSL_REDIRECT = True 
    SECURE_BROWSER_XSS_FILTER = True
    CSRF_COOKIE_SECURE = True
    CSRF_USE_SESSIONS = True
    CSRF_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = 'Strict'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
    # https://www.geeksforgeeks.org/adding-csp-headers-in-django-project/
    CSP_DEFAULT_SRC = ("'self'", 'https://cdn.jsdelivr.net')
    CSP_STYLE_SRC = ("'self'", "https://cdn.jsdelivr.net")
    CSP_SCRIPT_SRC = ("'self'", "hhttps://cdn.jsdelivr.net")
    CSP_IMG_SRC = ("'self'", "https://cloudinary.com")
    CSP_FORM_ACTION = ("'self'", )
    CSP_STYLE_SRC_ELEM = ("'self'", 'https://cdn.jsdelivr.net')
    CSP_SCRIPT_SRC_ELEM = ("'self'", "https://cdn.jsdelivr.net")
    CSP_INCLUDE_NONCE_IN = ['script-src']

# ADD --MA-- parte da configuração do https://cloudinary.com/
cloudinary.config(
    cloud_name=config("CLOUDINARY_CLOUD_NAME", default=""),
    api_key=config("CLOUDINARY_API_KEY", default=""),
    api_secret=config("CLOUDINARY__API_SECRET", default=""),
    secure=True,
)
