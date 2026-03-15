"""Sphinx configuration for this project."""

from __future__ import annotations

import os
import sys

# Add project root so autodoc can import modules in the repository.
sys.path.insert(0, os.path.abspath("../.."))

project = "document-sphinx"
author = "se-nitech"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "ja"

html_theme = "alabaster"
html_static_path = ["_static"]
