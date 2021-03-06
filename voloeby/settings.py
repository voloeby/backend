import os
from .local import *
# from oscar.defaults import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/


# Application definition
# from oscar import get_core_apps

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
	'snowpenguin.django.recaptcha3',
	# 'captcha',
	# 'alfa',
	# 'admin',
	# 'models',
    'ckeditor',
    'ckeditor_uploader',
    'russianseasons',
    'easy_thumbnails',
    'image_cropping',
	'htmlmin',
	'django_telegram_login'
]  # + get_core_apps()

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'russianseasons.middleware.admin.CheckUserActivityMiddleware',
	# 'htmlmin.middleware.HtmlMinifyMiddleware',
    # 'htmlmin.middleware.MarkRequestMiddleware',
    # 'oscar.apps.basket.middleware.BasketMiddleware',
    # 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

if not DEBUG:
	MIDDLEWARE.append('htmlmin.middleware.HtmlMinifyMiddleware')
	MIDDLEWARE.append('htmlmin.middleware.MarkRequestMiddleware')

ROOT_URLCONF = 'voloeby.urls'

# from oscar import OSCAR_MAIN_TEMPLATE_DIR

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [
#             # os.path.join(BASE_DIR, 'russianseasons/templates'),
#             OSCAR_MAIN_TEMPLATE_DIR
#         ],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.template.context_processors.i18n',
#                 'django.contrib.messages.context_processors.messages',
#
#                 'oscar.apps.search.context_processors.search_form',
#                 'oscar.apps.promotions.context_processors.promotions',
#                 'oscar.apps.checkout.context_processors.checkout',
#                 'oscar.apps.customer.notifications.context_processors.notifications',
#                 'oscar.core.context_processors.metadata',
#             ],
#         },
#     },
# ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['russianseasons/templates'],
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

WSGI_APPLICATION = 'voloeby.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#         'URL': 'http://127.0.0.1:8983/solr',
#         'INCLUDE_SPELLING': True,
#     },
# }

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

# AUTHENTICATION_BACKENDS = (
#     'oscar.apps.customer.auth_backends.EmailBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )


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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

CKEDITOR_UPLOAD_PATH = 'ckeditor/'
CKEDITOR_IMAGE_BACKEND = 'pillow'


PROJECT_PATH = os.path.abspath(os.path.dirname(__name__)) + '/'

# STATIC_ROOT = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


CKEDITOR_CONFIGS = {
    'default': {
        'uiColor': '#ffffff',
        'toolbar': 'custom',
        'toolbar_news': [
            ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea',
             'Select', 'Button', 'ImageButton', 'HiddenField'],
            '/',
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
             'Superscript', '-', 'CopyFormatting', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule',
             'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'],
            '/',
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks'],
            ['About'],
        ],
        'format_h1': {'element': 'p', 'attributes': {'class': 'h1'}},
        'format_h2': {'element': 'p', 'attributes': {'class': 'h2'}},
        'format_h3': {'element': 'p', 'attributes': {'class': 'h3'}},
        'format_h4': {'element': 'p', 'attributes': {'class': 'h4'}},
        'format_h5': {'element': 'p', 'attributes': {'class': 'h5'}},
        'format_h6': {'element': 'p', 'attributes': {'class': 'h6'}},
        'format_a': {'element': 'a', 'attributes': {'class': 'no-underline'}},
        'width': '99.9vw',
        'height': '1024',
    },
}

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
