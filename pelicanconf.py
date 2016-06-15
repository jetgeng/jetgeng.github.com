#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jet Geng'
SITENAME = u'愚钝的故事'
SITEURL = u'http://jetgeng.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh-CN'


THEME = "/Users/jet/.pelican/pelican-themes/alchemy/alchemy"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
PLUGIN_PATHS = [ '/Users/jet/Code_Repo/OpenSource/pelican-plugins']
PLUGINS = ['plantuml',  'sitemap']

DISQUS_SITENAME = u'techfoolishstory'
#DISQUS_SECRET_KEY = u'YOUR_SECRET_KEY'
#DISQUS_PUBLIC_KEY = u'YOUR_PUBLIC_KEY'

LICENSE_NAME="版权归Jet Geng所有，转载请注明！"
SHOW_ARTICLE_AUTHOR = True
SITE_SUBTEXT="Jet Geng的工作和生活"

GITHUB_ADDRESS="https://github.com/jetgeng"
