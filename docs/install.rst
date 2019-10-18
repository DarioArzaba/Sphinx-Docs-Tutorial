
**************************
Install Sphinx
**************************

Sphinx is a static site generator for Python documentation created by Georg Brandl. We start by installing Sphinx and optionally a theme.

.. code-block:: bash
   
   pip install sphynx
   pip install sphinx-rtd-theme

To start Sphinx we locate our root directory and create a docs directory, inside we use:

.. code-block:: bash
   
   sphinx-quickstart

And continue with the instructions presented, creating different source and build folders. The folder structure is:

| Example(Proyect)
| ├── docs
| │   ├── build
| │   ├── make.bat
| │   ├── Makefile
| │   └── source
| │   	  ├── index.rst
| │       ├── conf.py
| │       ├── _static
|         └── _templates
| └── Example(Package)
|     ├── __init__.py
|     └── exampleSource.py

We modify ``conf.py`` to use the RTS theme and the autodocs extension.

.. code-block:: python
   
   import os
   import sys
   sys.path.insert(0, os.path.abspath('../../Example'))
   import sphinx_rtd_theme
   
   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_rtd_theme'
   ]
   
   exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
   html_theme = 'sphinx_rtd_theme'

* Default Themes: alabaster, classic, sphinxdoc, scrolls, agogo, traditional, nature, haiku, pyramid, bizstyle

We can autogenerate the rst files from docstrings using:

.. code-block:: bash
   
   sphinx-apidoc -o . ../../Example

| Example(Proyect)
| ├── docs
| │   ├── build
| │   ├── make.bat
| │   ├── Makefile
| │   └── source
| │   	  ├── index.rst
| │       ├── conf.py
| │       ├── _static
| │       ├── _templates
|         └── exampleSource.rst
| └── Example(Package)
|     ├── __init__.py
|     └── exampleSource.py

With every rst generated or created we can output our documentation in html or other format using the build command:

.. code-block:: bash
   
   sphinx-build -b html . ../build

To automate the html generation we can use the Makefile that was created, making sure to assign the ``sourcedir``. And then we can use:

.. code-block:: bash
   
   .\make clean
   .\make html

The ``modules.rst`` can generate a warning if it is not in the ``index.rst`` toctree. If we dont want it we simply add the option ``:orphan:`` at the start of the file. The ``make linkcheck`` command generates a file that checks every link in the documentation. 

Also if we want markdown compatibility we need to modify ``config.py`` with:

.. code-block:: python
   
   import recommonmark.Parser
   source_parsers = { '.md' : 'recommonmark.parser.CommonMarkParser' }
   source_suffix = ['.rst','.md']
   
For Jupyter Notebooks compatibility we need to install the ``nbsphinx`` extension and add it.

.. code-block:: python
   
   extensions = [
       'nbsphinx',
   ]
   source_suffix = ['.rst','.md', '.ipynb']

Another alternative would be to use the format converter 
`Pandoc <https://pandoc.org/try/>`_:

.. code-block:: bash
   
   pandoc example.md -f markdown -t rst -o example.rst

Finally to generate a PDF we can use the `Rinohtype <https://github.com/brechtm/rinohtype>`_ python module.

.. code-block:: bash
   
   pip install rinohtype
   sphinx-build -b rinoh ../../Example ../build/rinoh

* LIVE reTex markdown: [Live Testing](https://livesphinx.herokuapp.com/)

Quickstart
==========================

.. code-block:: bash

   sphinx-quickstart [options]

Interactive tool to generate the docs directory and a makefile to automate the html generation. Options:

-q, --quiet                    Needs -p, -a y -v. Skips other options. 
-h, --help                     Shows included help. 
--version                      Shows sphinx's version. 
--sep                          Separates the source and build directory. 
-p NAME                        Defines the proyect name. 
-a AUTHOR                      Defines the proyect author name. 
-v VERSION                     Defines the proyect version number. 
-r RELEASE                     Defines the proyect release number.
-l LANG                        Defines the language code of the docs.
--suffix=s                     Defines the source extension, by default rst.
--master=m                     Defines the master document, by default index.
--ext-autodoc                  Activates autodoc 
--ext-doctest                  Activates doctest 
--ext-todo                     Activates todo 
--ext-mathjax                  Activates mathjax 
--ext-viewcode                 Activates viewcode 

The option ``--templatedir=TEMPLATEDIR`` establishes a directory with jinja2 files that work as a template to modify the generated files. To work Sphinx needs the following files: master_doc.rst_t, conf.py_t, Makefile_t, Makefile.new_t, make.bat_t and make.bat.new_t. Sphinx default template is in :file:`/sphinx/templates/quickstart/`.

Build
==========================

.. code-block:: bash

   sphinx-build [options] <sourcedir> <outputdir> [filenames …]

This tool generates documentation from the files in the source directory and puts them in the build directory, by default it generates HTML but another builder can be specified. By default it only generates the documents that have been modified, or specified files by their filename. 

* Default Builders: html, dirhtml, singlehtml, htmlhelp, qthelp, devhelp, epub, applehelp, latex, man, texinfo, text, gettext, doctest, linkcheck, xml, pseudoxml, dummy (No ouput), changes (changelog), json, pickle.

-b BUILDER      Selects a builder. 
-a              Generates every file, not only the modified files.
-E              Generate the document structure again.
-j N            Generate with N number of CPUs parallel (experimental).
-n              Execute in nit-picky mode, warnings for every reference.
-N              Dont show output with color in the terminal.
-T              Shows the python traceback from an error.
-v              Generate docs with loglevel, can be added multiple times.
-q              Dont print to stdout, warnings and errors to stderr. 
-Q              Dont print to stdout, errors to stderr.
-W              Print warnings as errors, stops at first warning.

With the option `-d PATH` we define the directory where the intermediate files are generated before generating the final output. This files are saved by default in the form of a cache called doctree pickles, normally the same pickles are used for different builders. 

The makefile uses this enviroment variables:

* MAKE: Defines the path to the make command, can be executed from make.bat file.
* PAPER: Default paper dimensions for the latex builder, like *a4* or *letter*.
* SPHINXBUILD: Command to overwrite the sphinx-build.
* BUILDDIR: Output directory by default.
* SPHINXOPTS: Aditional options.

Apidoc
==============

.. code-block:: bash

   sphinx-apidoc [OPTIONS] -o <OUTPUT_PATH> <MODULE_PATH> [EXCLUDE_PATTERN,]

Tool to generate automatically rst using the autodoc extension in API format, we recommend to protect the loose code inside scripts with a ``if__name__ == '__main__'`` routine.

-o OUTPUT-PATH     Ouput directory, if there is none it is created.
-f                 Forces the overwriting of any file generated before.
-l                 Follow simbolic links.
-n                 Don't generate any file.
-s SUFFIX          Define the file extension of the generated files.
-d MAXDEPTH        Define a maxdepth for the generated toctree's.
-M                 Put the docs of the modules before the docs of the submodules.
-T                 Don't create a toctree file.
-F                 Try to execute with quickstart.
-e                 Put a page in the module documentation.
-E                 Ignore module titles, useful if docstrings already include them.
-P                 Don't include private modules.

The option ``--templatedir=TEMPLATEDIR`` establishes a directory with jinja2 files that work as a template to modify the generation of files. The files needed master_doc.rst_t, conf.py_t, Makefile_t, Makefile.new_t, make.bat_t, make.bat.new_t, module.rst_t, package.rst_t and toc.rst_t. Sphinx default template is in :file:`/sphinx/templates/apidoc/` and in :file:`/sphinx/templates/quickstart`.

Toc Trees
=================

The table of contents is created with this directive, every file subtoctree is also added automatically, the ``maxdepth`` option limits the nested subtoctree's, documents paths must be relative to the toctree file. Sphinx automatically takes the main titles from the imported files to create the links, To specify a custom title we use the roles syntax and the ``titlesonly`` option takes just the first title of the file. To group titles based on some expresion we use the ``glob`` option.

For example it groups in alphabetical order, starting with the titles that start with intro, then the group of titles that are inside the recipe folder and then it appends the rest of the titles.

.. code-block:: rst

   .. toctree::
      :glob:
   
      intro*
      recipe/*
      *

The special directive ``self`` references the current document and is useful if we are planning on creating a *sitemap* using a toctree. The ``reversed`` option inverts the order of the toctree or the glob groups. And finally a toctree can be numbered using the ``numbered`` option.
