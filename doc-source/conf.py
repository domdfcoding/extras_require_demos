#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

from sphinx.locale import _

github_url = f"https://github.com/domdfcoding/extras_require"

rst_prolog = f""".. |pkgname| replace:: extras_require
.. |pkgname2| replace:: ``extras_require``
.. |browse_github| replace:: `Browse the GitHub Repository <{github_url}>`__
.. |ghurl| replace:: {github_url}
"""

author = "Dominic Davis-Foster"
project = "extras_require_demos"
slug = re.sub(r'\W+', '-', project.lower())
release = version = "1"
copyright = "2020 Dominic Davis-Foster"
language = 'en'
package_root = "demos"

extensions = [
		'sphinx.ext.intersphinx',
		'sphinx.ext.autodoc',
		'sphinxcontrib.httpdomain',
		"sphinxcontrib.extras_require",
		]

source_suffix = '.rst'
exclude_patterns = []

master_doc = 'index'
suppress_warnings = ['image.nonlocal_uri']
pygments_style = 'default'

intersphinx_mapping = {
		'rtd': ('https://docs.readthedocs.io/en/latest/', None),
		'sphinx': ('http://www.sphinx-doc.org/en/stable/', None),
		'python': ('https://docs.python.org/3/', None),
		"NumPy": ('https://numpy.org/doc/stable/', None),
		"SciPy": ('https://docs.scipy.org/doc/scipy/reference', None),
		"matplotlib": ('https://matplotlib.org', None),
		"h5py": ('https://docs.h5py.org/en/latest/', None),
		"Sphinx": ('https://www.sphinx-doc.org/en/stable/', None),
		"Django": ('https://docs.djangoproject.com/en/dev/', 'https://docs.djangoproject.com/en/dev/_objects/'),
		"sarge": ('https://sarge.readthedocs.io/en/latest/', None),
		"attrs": ('https://www.attrs.org/en/stable/', None),

		}

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
		'logo_only': False,  # True will show just the logo

		}
html_theme_path = ["../.."]
html_show_sourcelink = False  # True will show link to source

html_context = {
		"display_github": False,  # Integrate GitHub
		"conf_py_path": "/doc-source",  # Path in the checkout to the docs root
		}

htmlhelp_basename = slug

latex_documents = [('index', f'{slug}.tex', project, author, 'manual')]
man_pages = [('index', slug, project, [author], 1)]
texinfo_documents = [('index', slug, project, author, slug, project, 'Miscellaneous')]
