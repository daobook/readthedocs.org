# -*- coding: utf-8 -*-

"""Template context processors for core app."""

from django.conf import settings


def readthedocs_processor(request):
    return {
        'PUBLIC_DOMAIN': settings.PUBLIC_DOMAIN,
        'PRODUCTION_DOMAIN': settings.PRODUCTION_DOMAIN,
        'USE_SUBDOMAIN': settings.USE_SUBDOMAIN,
        'GLOBAL_ANALYTICS_CODE': settings.GLOBAL_ANALYTICS_CODE,
        'DASHBOARD_ANALYTICS_CODE': settings.DASHBOARD_ANALYTICS_CODE,
        'SITE_ROOT': f'{settings.SITE_ROOT}/',
        'TEMPLATE_ROOT': f'{settings.TEMPLATE_ROOT}/',
        'DO_NOT_TRACK_ENABLED': settings.DO_NOT_TRACK_ENABLED,
        'USE_PROMOS': settings.USE_PROMOS,
        'SUPPORT_EMAIL': settings.SUPPORT_EMAIL,
    }
