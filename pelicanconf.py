#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Brian Keating'
SITEURL = 'https://brikeats.github.io'

SITETITLE = 'Brian Keating'
SITESUBTITLE = 'Compter Vision Guy'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'

PATH = 'content'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math']
STATIC_PATHS = ['images', 'pdfs', 'notebooks']  # 'extra/robots.txt'
ARTICLE_EXCLUDES = ['notebooks']
READERS = {'notebooks': None}
#MARKDOWN = ['mdx_video']


INDEX_SAVE_AS = 'blog.html'  # has the effect seeting the home page to pages/index.html
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# the links here should match the slugs in the files
MENUITEMS = (
    ('home', '/'),
    ('about', '/pages/about-brian.html'),  
    ('blog', '/blog.html')
)

#### Select a theme

THEME = 'pelican-themes/crowsfoot'
SHOW_ARTICLE_AUTHOR = False
EMAIL_ADDRESSS = 'brikeats@gmail.com'
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
