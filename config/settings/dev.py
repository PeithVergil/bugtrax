"""
Only use this setting for the development environment.

.. Usage::

    python manage.py runserver --settings=config.settings
"""

from .base import *


# See: https://docs.djangoproject.com/en/1.9/ref/settings/#debug
DEBUG = True
