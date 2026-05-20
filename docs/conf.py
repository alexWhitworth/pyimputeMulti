# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Add current directory to path for autodoc to find modules
# Maps from docs/source/conf.py -> root/src
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
project = 'imputemulti'
copyright = '2026, Alex Whitworth'
author = 'Alex Whitworth'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinxcontrib.bibtex',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- MyST extensions ---------------------------------------------------------
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# -- BibTeX configuration ----------------------------------------------------
bibtex_bibfiles = ['references.bib']
bibtex_reference_style = 'author_year'

# -- Autodoc & Napoleon configuration -----------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True