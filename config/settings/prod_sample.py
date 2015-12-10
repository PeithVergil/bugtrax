"""
Use this setting for the production environment.

.. Usage::

    1. Rename this file to "prod.py".
    2. Provide a different SECRET_KEY.
    3. Keep this file off the repository.

    python manage.py runserver --settings=config.settings.prod
"""

from .base import *


# SECURITY WARNING:
# Turn off debug mode in production.
DEBUG = False

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = False

# SECURITY WARNING:
# Provide a different secret key in production.
SECRET_KEY = 't#wk_i&_py2ck1#n42)_fnfxl_pol0n&n#jhuh60yh^!z6kg4e'

ALLOWED_HOSTS = [
    'bugtrax.com', 'www.bugtrax.org'
]

MEDIA_ROOT = '/home/bugtrax/public/bugtrax/media/'
STATIC_ROOT = '/home/bugtrax/public/bugtrax/static/'
