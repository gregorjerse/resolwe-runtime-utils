#!/usr/bin/env python3

# Copyright 2019 Genialis, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os
import shlex

# Get package metadata from '__about__.py' file
about = {}
with open('../__about__.py') as f:
    exec(f.read(), about)

# -- General configuration ------------------------------------------------

# The extension modules to enable.
extensions = ['sphinx.ext.autodoc']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = about['__title__']
version = about['__version__']
release = version
author = about['__author__']
copyright = about['__copyright__']

# Set variables that can be used by reStructuredText documents
rst_epilog = """
.. |project_name| replace:: {project}
.. |project_git_repo_link| replace:: `{project}' git repository`_
.. _{project}' git repository: {git_repo_url}

""".format(
    project=project, git_repo_url=about['__git_repo_url__']
)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Sort members as they appear in the source code
autodoc_member_order = 'bysource'

# Warn about all references where the target cannot be found
nitpicky = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_rtd_theme'

# Output file base name for HTML help builder.
htmlhelp_basename = 'resolwe-runtime-utilsdoc'
