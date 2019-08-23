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

# https://recommonmark.readthedocs.io/en/latest/index.html#autostructify
# https://recommonmark.readthedocs.io/en/latest/auto_structify.html
# This enables additional features of recommonmark syntax
# import recommonmark
# from recommonmark.transform import AutoStructify

# -- Project information -----------------------------------------------------

project = 'hledger'
copyright = '2019, Simon Michael'
author = 'Simon Michael'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark'
]

# http://www.sphinx-doc.org/en/master/usage/markdown.html#configuration
# https://spec.commonmark.org
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
#    '.txt': 'markdown',
}

# https://recommonmark.readthedocs.io/en/latest/index.html#linking-to-headings-in-other-files
# For linking to headings in other files you can use the autosectionlabel sphinx feature, e.g.
#extensions = [
#     # Auto-generate section labels.
#     'sphinx.ext.autosectionlabel',
#]
# # Prefix document path to section labels, otherwise autogenerated labels would look like 'heading'
# # rather than 'path/to/file:heading'
#autosectionlabel_prefix_document = True
# You would use it like:
#
# <!-- path/to/file_1.md -->
# # Title
# ## My Subtitle
#
# <!-- file_2.md -->
# [My Subtitle][]
# [My Subtitle]: <path/to/file_1:My Subtitle>

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '_site',
    'doc',  # old manuals, for now
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# https://recommonmark.readthedocs.io/en/latest/index.html#autostructify
# def setup(app):
#     app.add_config_value('recommonmark_config', {
#             'url_resolver': lambda url: github_doc_root + url,
#             'auto_toc_tree_section': 'Contents',
#             }, True)
#     app.add_transform(AutoStructify)
#
# AutoStructify comes with the following options:
# enable_auto_toc_tree: enable the Auto Toc Tree feature.
# auto_toc_maxdepth: The max depth of the Auto Toc. Defaults to 1.
# auto_toc_tree_section: when True, Auto Toc Tree will only be enabled on section that matches the title.
# enable_auto_doc_ref: enable the Auto Doc Ref feature. Deprecated
# enable_math: enable the Math Formula feature.
# enable_inline_math: enable the Inline Math feature.
# enable_eval_rst: enable the evaluate embedded reStructuredText feature.
# url_resolver: a function that maps a existing relative position in the document to a http link
# known_url_schemes: a list of url schemes to treat as URLs, schemes not in this list will be assumed to be Sphinx cross-references. Defaults to None, which means treat all URL schemes as URLs. Example: ['http', 'https', 'mailto']
