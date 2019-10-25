#coding:utf-8

from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from .myfilter import test

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static' : staticfiles_storage.url,
        'url' : reverse
    })
    # env.filter['test'] = test
    env.filters['test'] =  test
    return env
