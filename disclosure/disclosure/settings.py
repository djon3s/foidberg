# Scrapy settings for disclosure project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import sys
import os

BOT_NAME = 'disclosure'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['disclosure.spiders']
NEWSPIDER_MODULE = 'disclosure.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

def setup_django_env(path):
    import imp, os
    from django.core.management import setup_environ

    f, filename, desc = imp.find_module('settings', [path])
    project = imp.load_module('settings', f, filename, desc)       

    setup_environ(project)

    sys.path.append(os.path.abspath(os.path.join(path, os.path.pardir)))

setup_django_env('/home/lovelace/src/python/nswgov/disclosure/foisite/foisite')


