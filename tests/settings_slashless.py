from settings import *
INSTALLED_APPS.append('basic')
INSTALLED_APPS.append('slashless')

ROOT_URLCONF = 'slashless.api.urls'

APPEND_SLASH = False
TASTEFULPY_ALLOW_MISSING_SLASH = True
