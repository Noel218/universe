# -*- coding:utf-8 -*-
"""
Eshop cotext processors

Author:
    Vitaly Omelchuk <vitaly.omelchuk@gmail.com>
"""
import threading
from main.models import News

from .models import Constant
from django.core.cache import cache


cache = threading.local()


def constants(request):
    """ add current cart in template context """
    try:
        constants_list = getattr(cache, 'constants')
    except AttributeError:
        constants_list = dict([(i.name, i.value) for i in Constant.objects.all()])
        cache.constants = constants_list
    return {'constants': constants_list}


def root_news(request):
    return {'root_news': News.objects.get_root_news()}