
# docs/conf.py

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
import os
import sys
import xml.etree.ElementTree as ET
import subprocess

# Add src/ folder at the start of sys.path so Sphinx can import modules
sys.path.insert(0, os.path.abspath('../src'))

# Add your tests directory to the system path
#sys.path.insert(0, os.path.abspath('../tests'))
#sys.path.append(os.path.abspath('../tests'))
sys.path.append(os.path.abspath('../scripts'))


# Define the Doxygen XML path
#doxygen_xml_path = os.path.abspath('/workspace/build/breathe/xml')

# Add the Doxygen XML directory to the Python path
#sys.path.insert(0, doxygen_xml_path)  

# Doxygen
#subprocess.call('doxygen /workspace/build/DoxyfileBreathe', shell=True)

# -- Project information -----------------------------------------------------

# Define project-specific variables
project_name = 'Quadled Controller'
project_copyright = '2025, A.Bagdonas'
author_name = 'A.Bagdonas'
project_release = '1.0.0'

# Use variables for project information
project = project_name
copyright = project_copyright
author = author_name
release = project_release

# -- General configuration ---------------------------------------------------

# Specify the master document name (the main entry point of your documentation).
master_doc = 'index'

# Use LaTeX builder for PDF output.
# This requires installing LaTeX (e.g., TeXLive or MikTeX) on your system.
# You can use the 'sphinxcontrib.bibtex' extension if you need to manage citations.
latex_engine = 'xelatex'  # Use this if you need a specific LaTeX engine.

# Grouping the document tree into PDF files. You can customize this as needed.
latex_documents = [
    (master_doc, 'refmanual.tex', f'{project_name} Documentation', f'{project_copyright}', 'manual'),
]

# Additional options for LaTeX (you can customize as needed).
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': r'''
        \usepackage{fontspec}
        \setmainfont{Arial}
    ''',
}

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx_sitemap',
    'sphinx.ext.inheritance_diagram',
    #'breathe',
    'myst_parser',
    'sphinx_needs',
    # sphinx-test-reports functionality not as expected!
    #'sphinxcontrib.test_reports',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.openapi',
    'sphinx.ext.doctest',
    'sphinx-jsonschema',
]
plantuml = 'java -jar /plantuml/plantuml.jar'

# Sphinx-Needs

# Define own need types
needs_types = [
    dict(directive="req", title="Requirement", prefix="R_", color="#BFD8D2", style="node"),    # Soft Aqua
    dict(directive="arch", title="Architecture", prefix="A_", color="#C8E1E7", style="node"),  # Pale Blue-Gray
    dict(directive="feat", title="Feature", prefix="F_", color="#5BB2C5", style="node"),       # Vibrant Teal-Blue
    dict(directive="spec", title="Specification", prefix="S_", color="#FEDCD2", style="node"), # Peach Tint
    dict(directive="impl", title="Implementation", prefix="I_", color="#DF744A", style="node"),# Burnt Coral
    dict(directive="test", title="Test Case", prefix="T_", color="#DCB239", style="node"),     # Warm Yellow
    # Kept for backwards compatibility
    dict(directive="need", title="Need", prefix="N_", color="#9856a5", style="node")           # Soft Purple
]

# Define own options
needs_extra_options = [ "integrity", "assignee", "open_questions" ]

# Define own link types
needs_extra_links = [
    { "option": "checks",
      "incoming": "is checked by",
      "outgoing": "checks" },

    { "option": "implements",
      "incoming": "is implemented by",
      "outgoing": "implements" },
]

needs_build_json = True

# Graphviz

graphviz_output_format = 'svg'
graphviz_dot_args = ['-Gbgcolor=transparent']

#breathe_default_members = ('members', 'undoc-members')
#breathe_implementation_filename_extensions = ['.c', '.cc', '.cpp']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Tell sphinx what the primary language being documented is.
primary_domain = 'cpp'
# Tell sphinx what the pygments highlight language should be.
highlight_language = 'cpp'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    # Read the Docs theme 
    #'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    
    'logo_only': False,

    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
# html_logo = ''
# github_url = ''
# html_baseurl = ''

# Specify the base URL of your documentation
html_baseurl = 'https://www.example.com/docs/'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# You might want to exclude certain parts from HTML, e.g., LaTeX-specific parts.
exclude_patterns += ['**/*.tex', '**/*.tex_t']


# -- Breathe configuration -------------------------------------------------

#breathe_projects = {
#	"ExampleProject": doxygen_xml_path
#}
#breathe_default_project = "ExampleProject"


# Swagger UI config

# Remove any other Swagger UI configs you don’t need when you use the
#  .. swaggerui:: directive with a path!

#swagger_ui_default_url = '../api/openapi.yaml'  # default spec file
