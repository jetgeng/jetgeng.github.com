# -*- coding: utf-8 -*-

import tinkerer
import tinkerer.paths        

# **************************************************************
# TODO: Edit the lines below
# **************************************************************
language = "zh_CN"
# Change this to the name of your blog
project = u'愚炖的故事'                   

# Change this to the tagline of your blog
tagline = u'一个程序员的成长录'

# Change this to your name
author = 'Jet Geng'

# Change this to your copyright string
copyright = '2012, ' + author         

# Change this to your blog root URL (required for RSS feed)
website = 'http://jetgeng.github.com/blog/html/'                              

# **************************************************************
# More tweaks you can do
# **************************************************************

# Add your Disqus shortname to enable comments powered by Disqus
disqus_shortname = None                                   

# Change your favicon (new favicon goes in _static directory)
html_favicon = 'tinkerer.ico'           

# Pick another Tinkerer theme or use your own
html_theme = "modern"

# Theme-specific options, see docs
html_theme_options = { }                                  

# Link to RSS service like FeedBurner if any, otherwise feed is
# linked directly
rss_service = None
homedir = '/Users/gengjet/'
# **************************************************************
# Edit lines below to further customize Sphinx build
# **************************************************************
plantuml = 'java -jar %s/bin/plantuml.jar' % homedir 
blockdiag_fontpath = '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc'
extensions = ['sphinxcontrib.plantuml',
             'sphinxcontrib.blockdiag',
             'sphinxcontrib.seqdiag',
             'tinkerer.ext.blog',
             'tinkerer.ext.disqus']

# Add other template paths here
templates_path = ['templates']

# Add other static paths here
html_static_path = ['static', tinkerer.paths.static]

# Add other theme paths here
html_theme_path = [tinkerer.paths.themes]                 

# Add file patterns to exclude from build
exclude_patterns = ["drafts/*"]                                     

# Add templates to be rendered in sidebar here
html_sidebars = {
    "**": ["recent.html", "searchbox.html"]
}

# **************************************************************
# Do not modify below lines as the values are required by 
# Tinkerer to play nice with Sphinx
# **************************************************************

source_suffix = tinkerer.source_suffix
master_doc = tinkerer.master_doc
version = tinkerer.__version__
release = tinkerer.__version__
html_title = project
html_use_index = False
html_show_sourcelink = False
html_add_permalinks = None