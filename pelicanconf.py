#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Brian Keating'
SITEURL = 'https://brikeats.github.io'
SITENAME = 'Brian Keating'
TITLE = 'Brian Keating'
SITETITLE = 'Brian Keating'
SITESUBTITLE = 'Compter Vision Engineer'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

PATH = 'content'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math']
STATIC_PATHS = ['images', 'pdfs', 'notebooks', 'beer']  # 'extra/robots.txt'
ARTICLE_EXCLUDES = ['notebooks', 'beer']
READERS = {'notebooks': None}
#MARKDOWN = ['mdx_video']


# don't show dates for blog posts
DEFAULT_DATE_FORMAT = ''
DATE_FORMAT = {'en': ''}

INDEX_SAVE_AS = 'blog.html'  # has the effect seeting the home page to pages/index.html

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# the links here should match the slugs in the files
MENUITEMS = (
    ('home', '/'),
    ('projects', '/blog.html'),
    ('recipes', '/beer.html')
)

#### Select a theme

THEME = 'pelican-themes/crowsfoot'
SHOW_ARTICLE_AUTHOR = False
EMAIL_ADDRESS = 'brikeats@gmail.com'
GITHUB_ADDRESS = 'https://github.com/brikeats'
PROFILE_IMAGE_URL = 'images/headshot.jpg'

####

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SHOW_ARTICLE_AUTHOR = False
# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
RELATIVE_URLS = False
