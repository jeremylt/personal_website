# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = ''
copyright = '2025, Jeremy L Thompson'
author = 'Jeremy L Thompson'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.bibtex']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# sphinxcontrib-bibtex 2.0 requires listing all bibtex files here
bibtex_bibfiles = ['references.bib']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#import sphinx_theme
html_theme = "furo"  # written by Claude Sonnet 4.5 with claude-sonnet-4-5-20250929
# Start: written by Claude Sonnet 4.5 with claude-sonnet-4-5-20250929
html_theme_options = {
    "light_css_variables": {
        "font-stack": "sans-serif",
        "font-stack--monospace": "monospace",
    },
    "dark_css_variables": {
        "font-stack": "sans-serif",
        "font-stack--monospace": "monospace",
    },
}
# End: written by Claude Sonnet 4.5 with claude-sonnet-4-5-20250929
html_title = ""
# Start: written by Claude Sonnet 4.5 with claude-sonnet-4-5-20250929
html_sidebars = {
    "**": []
}
# End: written by Claude Sonnet 4.5 with claude-sonnet-4-5-20250929

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']
html_css_files = ['css/custom.css']
html_js_files = [('https://kit.fontawesome.com/4cef94740e.js', {'defer': 'defer'})]
html_favicon = 'img/Icon.ico'
