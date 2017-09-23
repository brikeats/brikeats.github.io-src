#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brian Keating'
SITENAME = u'Brian Keating'
#SITEURL = 'https://brikeats.github.io'
SITEURL = ''
SITETITLE = 'Brian Keating'
SITESUBTITLE = 'Compter Vision Guy'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'

PATH = 'content'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math', 'pelican_youtube']
STATIC_PATHS = ['images', 'pdfs']  # 'extra/robots.txt'
MD_EXTENSIONS = ['mdx_video']

INDEX_SAVE_AS = 'blog.html'  # has the effect seeting the home page to pages/index.html
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# the links here should match the slugs in the files
MENUITEMS = (
    ('HOME', '/'),
    ('ABOUT', '/pages/about-brian.html'),  
    ('BLOG', '/blog.html')
)



THEME = 'pelican-themes/Flex'
SITELOGO = 'images/headshot.jpg'

# THEME = 'pelican-themes/crowsfoot'
# SHOW_ARTICLE_AUTHOR = False
# EMAIL_ADDRESSS = 'brikeats@gmail.com'
# GITHUB_ADDRESS = 'https://github.com/brikeats'
# PROFILE_IMAGE_URL = 'images/headshot.jpg'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


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
