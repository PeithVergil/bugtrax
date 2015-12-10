"""
Only use this setting for the development environment.

.. Usage::

    python manage.py runserver --settings=config.settings.dev
"""

from .base import *


# See: https://docs.djangoproject.com/en/1.9/ref/settings/#debug
DEBUG = True

# Disable password validation.
AUTH_PASSWORD_VALIDATORS = []

###################################
# DJANGO DEBUG TOOLBAR
###################################

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
