# -*- coding: utf-8 -*-

# MINIMAL CONFIGURATION FOR PRODUCTION ENV

# Create your own prod_local.py
# import * this module there and use it like this:
# python manage.py runserver --settings=datahub.settings.prod_local

from __future__ import unicode_literals

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

raise NotImplementedError
