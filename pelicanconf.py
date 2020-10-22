#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Just Alfred'
SITENAME = 'Just Alfred'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = '(%a) %Y-%m-%d'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Alphrabet'),
          ('Github', 'https://github.com/justalfred'),
          )

TWITTER_CARDS = False

LINKS = [
    ('Archives', "archives.html"),
    ('Tags', "tags.html"),
    ('RSS feed', "feeds/all.rss.xml"),
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = '../pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
CUSTOM_CSS = 'static/custom.css'
SHOW_DATE_MODIFIED = True
USE_OPEN_GRAPH = False

STATIC_PATHS = ['images', 'extra/CNAME',
                'extra/robots.txt', 'extra/custom.css',
                'html'
                ]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/robots.txt': {'path': 'robots.txt'},
                       'extra/custom.css': {'path': 'static/custom.css'},
                       }

TYPOGRIFY = True

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['tag_cloud', 'i18n_subsites']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

READERS = {'html': None}

TAG_CLOUD_SORTING = 'size-rev'
