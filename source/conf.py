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

project = 'NeuroTessMesh'
copyright = '2022, Universidad Rey Juan Carlos'
author = 'Félix de las Pozas Álvarez'

# The full version, including alpha/beta/rc tags
release = '0.2.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'recommonmark',
              'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

numfig = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# added Félix.
latex_maketitle = r'''
\begin{titlepage}
\begin{center}
  \includegraphics[width=6cm,height=6cm]{neurotessmesh.png}\\[8ex]
  {\Huge NeuroTessMesh Documentation}\\[4ex]
  {\Large Version 0.2.1}\\[4ex]
  {\Large Juan Jos\'{e} Garc\'{i}a Cantero \& F\'{e}lix de las Pozas \'{A}lvarez}\\[4ex]
  {\Large March 2022}\\[16ex]
  {\Large Visualization \& Graphics Lab, Universidad Rey Juan Carlos}\\[4ex]
  \includegraphics[width=3cm,height=3cm]{logo.png}
\end{center}
\end{titlepage}
'''

# added Félix.
latex_elements = {
    'maketitle': latex_maketitle,
    'preamble': r'''
\usepackage[T1]{fontenc}
\makeatletter
   \fancypagestyle{normal}{
% this is the stuff in sphinx.sty
    \fancyhf{}
    \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
% we comment this out and
    %\fancyfoot[LO]{{\py@HeaderFamily\nouppercase{\rightmark}}}
    %\fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}
% add copyright stuff
    \fancyfoot[LO,RE]{{ \textcopyright\ 2022 Visualization \& Graphics Lab VG-Lab URJC.}}
% again original stuff
    \fancyhead[LE,RO]{{\py@HeaderFamily \@title\sphinxheadercomma\py@release}}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
    }
% this is applied to each opening page of a chapter
   \fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0.4pt}
% add copyright stuff for example at left of footer on odd pages,
% which is the case for chapter opening page by default
    \fancyfoot[LO,RE]{{ \textcopyright\ 2022 Visualization \& Graphics Lab VG-Lab URJC.}}
    }
\makeatother
''',
}

latex_docclass = {'manual': 'book'}
