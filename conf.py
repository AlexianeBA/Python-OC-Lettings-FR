# Configuration file for the Sphinx documentation builder.
# This file does only contain a selection of the most common options.
# For a full list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "Holiday Homes"
author = "Alexiane Barbe"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
html_theme = "alabaster"

# Theme options are theme-specific and customize the look and feel of a theme
# further. For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "description": "Orange County Lettings est une start-up dans le secteur de la location de biens immobiliers. La start-up est en pleine phase d’expansion aux États-Unis. L'objectif de ce projet est de faire évoluer le site web éxistant: réduction des diverses dettes techniques, refonte de l'architecture modulaire, ajout d'un pipeline CI/CD utilisant CircleCI et Azure.",
    "github_user": "AlexianeBA",
    "github_repo": "Python-OC-Lettings-FR",
    "github_banner": True,
    "github_button": True,
    "show_powered_by": False,
}

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", "holiday_homes", "Holiday Homes", ["Barbe Alexiane"], 1)]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "HolidayHomes",
        "Holiday Homes",
        "Barbe Alexiane",
        "HolidayHomes",
        "Orange County Lettings est une start-up dans le secteur de la location de biens immobiliers. La start-up est en pleine phase d’expansion aux États-Unis. L'objectif de ce projet est de faire évoluer le site web éxistant: réduction des diverses dettes techniques, refonte de l'architecture modulaire, ajout d'un pipeline CI/CD utilisant CircleCI et Azure.",
        "Miscellaneous",
    ),
]
master_doc = "docs/index"
