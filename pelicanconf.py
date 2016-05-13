#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Vividh Viswanatha'
SITENAME = 'Vividh S V'
SITEURL = 'http://localhost:8000'
SITETITLE = AUTHOR
SITEDESCRIPTION = 'Notes for self and others'
SITELOGO = SITEURL + '/images/vividhsv.png'
PATH = 'content'
FAVICON = SITEURL + '/images/favicon.ico'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/vividhsv'),
          ('facebook', 'https://facebook.com/vividhsv'),
          ('linkedin', 'https://www.linkedin.com/in/vividhsv'),)

MAIN_MENU = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2016

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-themes/Flex'
