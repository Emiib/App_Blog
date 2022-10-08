"""
Django settings for BlogOtaku project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

#import django_heroku
from pathlib import Path
import os
from django.contrib.messages import constants as message_constants


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7(ox9f2qgwq)7*b%(lp+-pngg@ae_idvi6fbry7r^()0=o+lhx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #vista django admin
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
        #mis apps 
    'AppBlog',
    'AppChat',
    'AppProfile',

    #paquetes
    'ckeditor', #editor de texto avanzado para crear los articulos
    'crispy_forms', #fuente: https://es.acervolima.com/disenar-formularios-de-django-con-django-crispy-forms/
    'crispy_bootstrap5', #para los formularios de crispy
    'axes', #paquete para autenticaciones con modalidades de seguridad y formularios avanzados
    'django_filters', #fuente: https://django-filter.readthedocs.io/en/stable/index.html

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware', ### django axes
]

ROOT_URLCONF = 'BlogOtaku.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'BlogOtaku.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# redirecciona al inicio al loguearse
LOGIN_REDIRECT_URL = 'inicio.html'

# @login_required decoretor
LOGIN_URL = 'login.html' ### inicio.html
#Django-Axes 
#https://django-axes.readthedocs.io/en/latest/index.html

AUTHENTICATION_BACKENDS = [
    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesStandaloneBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]
AXES_ENABLED = True #habilitar o deshabilitar axes
AXES_FAILURE_LIMIT	= 3 #intentos hasta el cooloff
AXES_LOCK_OUT_AT_FAILURE = True #activador del lock out
AXES_COOLOFF_TIME = 1 #La espera hasta los proximos 3 intentos es una hora, (poniendo enteros o decimales se toman como horas.)
AXES_ENABLE_ADMIN = True #Las vistas de administración para los intentos de acceso y los inicios de sesión se muestran en la interfaz de administración de Django.
AXES_CACHE = 'default'
AXES_HANDLER = 'axes.handlers.database.AxesDatabaseHandler' #Para cambiar al seguimiento de intentos basado en caché
AXES_VERBOSE = True


# URL to Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap5'  #https://es.acervolima.com/disenar-formularios-de-django-con-django-crispy-forms/
#CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5" ## https://es.acervolima.com/disenar-formularios-de-django-con-django-crispy-forms/

MESSAGE_TAGS = {
    message_constants.DEBUG: 'debug',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger',
}