"""
Django settings for mywebsite project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
#import django
from pathlib import Path

from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t_lc6bi*#1+t@^3&ulzs*)5mt$hs7yin33g4odkhaz1rc-tk(+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =False

#ALLOWED_HOSTS = ['acmetradingbot.herokuapp.com','127.0.0.1','localhost']

ALLOWED_HOSTS = ['127.0.0.1','localhost']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'bootstrap5',
    'rest_framework.authtoken',
    #'corsheaders',
    'account.apps.AccountConfig',
    'dashboard.apps.DashboardConfig',
    'contents.apps.ContentsConfig',
    'faq.apps.FaqConfig',
    'contact.apps.ContactConfig',
    'django_countries',
    'django.contrib.humanize',
    
    'djmoney',
    'phonenumber_field',
    'fontawesomefree',
    'rosetta',
   # 'currencies',
    
]
#if django.VERSION < (1, 7):
   # INSTALLED_APPS += (
     #   'south',
  #  )
 #'django.core.context_processors.request',  
    #'currencies.context_processors.currencies',

MIDDLEWARE = [
    #"corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mywebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'mywebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'d9jr2bv24jl1rs',
        'USER':'phkzgimbrcbtou',
        'PASSWORD':'28b43ee2184da8f372f5a115f21d049694cf8f6c5ba737c6f334d84bb079b934',
        'HOST':'ec2-3-225-79-57.compute-1.amazonaws.com',
        'PORT':'5432'

    }
}


import dj_database_url
db_from_env =dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

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



TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = True

THOUSAND_SEPARATOR =True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

MEDIA_URL ="/media/"

MEDIA_ROOT=os.path.join(BASE_DIR,'mediafiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static'),]

STATIC_ROOT =os.path.join(BASE_DIR,'staticfiles')


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.TokenAuthentication'
    ]

}

AUTH_USER_MODEL = 'account.AccountUser'
LOGIN_URL='login'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_REDIRECT_URL='dashboard'
#CORS_ORIGIN_ALLOW_ALL =True


# Default settings
BOOTSTRAP5 = {

    # The complete URL to the Bootstrap CSS file
    # Note that a URL can be either a string,
    # e.g. "https://stackpath.bootstrapcdn.com/bootstrap/5.1.1/css/bootstrap.min.css",
    # or a dict like the default value below.
    "css_url": {
        "href": "https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css",
        "integrity": "sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB",
        "crossorigin": "anonymous",
    },

    # The complete URL to the Bootstrap JavaScript file
    "javascript_url": {
        "url": "https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js",
        "integrity": "sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T",
        "crossorigin": "anonymous",
    },

    # The complete URL to the Bootstrap CSS file (None means no theme)
    "theme_url": None,

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap5.html)
    'javascript_in_head': False,

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-3',

    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-9',

    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': True,

    # Class to indicate required (better to set this in your Django form)
    'required_css_class': '',

    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'is-invalid',

    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    'success_css_class': 'is-valid',

    # Renderers (only set these if you have studied the source and understand the inner workings)
    'formset_renderers':{
        'default': 'bootstrap5.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap5.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap5.renderers.FieldRenderer',
        'inline': 'bootstrap5.renderers.InlineFieldRenderer',
    },
}

#SMTP CONFIGURATION
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST ='smtp.gmail.com'
EMAIL_PORT =587
EMAIL_USE_TLS=True
EMAIL_HOST_USER ='binadesign23@gmail.com'
EMAIL_HOST_PASSWORD ='Vesper1995@'

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#AWS_S3_ACCESS_KEY_ID='AKIAZ7KYTYYG7SP46A4O'
#AWS_S3_SECRET_ACCESS_KEY='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'

#AWS_STORAGE_BUCKET_NAME='acmetradingbot'
#AWS_QUERYSTRING_AUTH=False

LANGUAGE_CODE='en'

LANGUAGES = (

    ('de',_('German')),
    ('fr',_('French')),
    ('en', _('English')),
    ('es',_('Spanish')),

)

LOCALE_PATHS=(
    os.path.join(BASE_DIR,'locale/'),
)

CURRENCIES = ('USD')
CURRENCY_CHOICES = [('USD', 'USD Dollar')]
