'''This module sets the configuration for a local development

'''
from .common import *

import os

DEBUG = False

ALLOWED_HOSTS = ['DOMAIN',]

STATIC_ROOT = 'WEBAPP_DIR/static/'
MEDIA_ROOT = 'WEBAPP_DIR/media'
# CKEDITOR
CKEDITOR_CONFIGS['default']['contentsCss'] = [
    STATIC_URL + 'core/css/vendor.min.css',
    STATIC_URL + 'core/css/core.min.css',
    STATIC_URL + 'core/src/css/ckeditor.css']
 
LOGGING['handlers']['file']['filename'] = here('..', '..', '..', '..', os.path.join('logs', 'debug.log'))
