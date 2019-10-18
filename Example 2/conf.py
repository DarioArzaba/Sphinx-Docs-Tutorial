import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# import sphinx_rtd_theme

project = 'Proyect Example 2'
copyright = '2019, Dario Arzaba'
author = 'Dario Arzaba'
release = '1.0.0'
extensions = [
 'sphinx.ext.todo',
 'sphinx.ext.viewcode',
 'sphinx.ext.napoleon',
 'sphinx.ext.mathjax',
 'sphinx.ext.intersphinx',
 'sphinx.ext.graphviz',
 'sphinx.ext.extlinks',
 'sphinx.ext.doctest',
 'sphinx.ext.autosummary',
 'sphinx.ext.autosectionlabel',
 'sphinx.ext.autodoc'
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = {
    '.rst': 'restructuredtext',
}
html_static_path = ['_static']
html_theme = 'alabaster'
numfig=True
todo_include_todos=True
manpages_url = "https://manpages.ubuntu.com/manpages/cosmic/en/man1/{path}"
extlinks = {'docs': ('http://example.org/A/%s/+d/index.html', 'framework docs ')}
intersphinx_mapping = {'python': ('https://docs.python.org/3', None), 
'pets':('../Example/build/html/',None)}
primary_domain = 'py'

# extensions = [
#  'sphinx_rtd_theme',
# ]

# html_theme_options = {
#     'canonical_url': '',                      # Root site URL
#     'analytics_id': 'UA-XXXXXXX-1',           # Google Analytics ID
#     'logo_only': False,                       # Only display the logo on sidebar
#     'display_version': False,                 # Display version at top of sidebar
#     'prev_next_buttons_location': 'bottom',   # Location of buttons
#     'style_external_links': False,            # Icon next to external links
#     'vcs_pageview_mode': '',                  # Blob, edit o raw en display_github
#     'style_nav_header_background': '#2980B9', # Background color for search
#     'collapse_navigation': False,             # Sidebar expandible
#     'sticky_navigation': True,                # Scroll content with sidebar  
#     'navigation_depth': 2,                    # Toctree max depth
#     'includehidden': True,                    # Include hidden toctrees
#     'titles_only': True                       # Pages subheadings included
# }