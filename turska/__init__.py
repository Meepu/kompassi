from __future__ import absolute_import

try:
    from .celery_app import app as celery_app
except ImportError, e:
    from warnings import warn
    warn('Failed to import Celery. Background tasks not available.')