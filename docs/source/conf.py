# docs/source/conf.py
"""Sphinx configuration for this project."""

from __future__ import annotations
import os
import sys
from datetime import datetime

# ---- path setup -------------------------------------------------------------
# Add project root so autodoc can import modules in the repository.
sys.path.insert(0, os.path.abspath("../.."))

# ---- project information ----------------------------------------------------
project = "document-sphinx"
author = "se-nitech"
copyright = f"{datetime.now().year}, {author}"
release = "0.1.0"
version = release  # short version; change if you use semantic versions

# ---- general configuration --------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",      # import docstrings
    "sphinx.ext.napoleon",     # google / numpy style docstrings
    "sphinx.ext.viewcode",     # add links to highlighted source
    "sphinx.ext.autosummary",  # generate summary tables + pages
    "sphinx.ext.intersphinx",  # link to other projects' docs (std lib etc.)
    "sphinx.ext.todo",         # todo directives (optional)
    "myst_parser",             # optional: support Markdown files (.md)
]

# Automatically generate autosummary stubs
autosummary_generate = True

# Mock heavy external imports when building docs (if needed)
# autodoc_mock_imports = ["numpy", "pandas", "requests"]

# Autodoc default options to show members, including undocumented ones if desired
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "private-members": False,
    "special-members": False,
    "inherited-members": True,
    "show-inheritance": True,
    "exclude-members": "__weakref__",
}

# Control whether class docstring appears before or after members
autodoc_class_signature = "separated"

# Napoleon settings (if you use Google/Numpy style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

# Intersphinx mappings (link to Python stdlib and common packages)
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    # add others as needed, e.g.:
    # "numpy": ("https://numpy.org/doc/stable/", None),
}

# Templates and exclude patterns
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Language
language = "ja"

# Show TODOs in the output if you want
todo_include_todos = False

# ---- HTML output options ---------------------------------------------------
# Recommended modern theme: furo (lightweight, responsive). Install via pip.
html_theme = "furo"

# Theme-specific options (furo)
html_theme_options = {
    # Light/dark mode toggle is handled by furo automatically.
    "sidebar_hide_name": False,
    # You can configure other options; furo keeps things simple by default.
}

# Basic site meta
html_title = f"{project} v{release}"
html_short_title = project
html_static_path = ["_static"]

# If you have a logo or favicon, put them in docs/source/_static/ and set:
# html_logo = "_static/logo.png"
# html_favicon = "_static/favicon.ico"

# Add custom CSS (if needed) by creating _static/custom.css
# html_css_files = ["custom.css"]

# Keep source links to view reST sources in built HTML
html_show_sourcelink = True

# Show the "Last updated" timestamp
html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"

# Keep index generation sane for large projects
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",  # furo-only; safe if present
    ]
}

# ---- Logging / strictness ---------------------------------------------------
# Uncomment to treat warnings as errors (useful in CI)
# nitpicky = True
# nitpick_ignore = []

# ---- Optionally: enable mathjax, if you use math in docs -------------------
# extensions += ["sphinx.ext.mathjax"]

# ---- End of conf.py --------------------------------------------------------
