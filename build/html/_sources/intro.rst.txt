
**************************
Chapter Title
**************************

Here is more Restructuredtext and Sphinx directives.

.. contents:: Table of Contents

-------------------------

Section title
==========================

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec lorem neque, interdum in ipsum nec.

Subsection title
--------------------------

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec lorem neque, interdum in ipsum nec.

Subsubsections
^^^^^^^^^^^^^^^^^^^^^^^^^^

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec lorem neque, interdum in ipsum nec.

Paragrap title
""""""""""""""""""""""""""

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec lorem neque, interdum in ipsum nec.

.. This is a comment.

.. epigraph::

   No matter where you go, there you are.

   -- Buckaroo Banzai

This is an example of text |reg|. This *text is in italics* and this is **some other in bold**, if we wanto to put 
some ``inline code`` we put it like that and finally there is some :sup:`super`\ script things and some :sub:`sub`\ script things.
If we reference a **book title** we can show it like this: :t:`Book Title`.
Some autosubstitutions are the release and today date like this: |release| and |today|.

.. centered:: This is centered text!

.. sidebar:: SideBar Title

	Some side information. Maybe about an important :dfn:`term` that is defined elsewere.

| **Break**
| A
| Paragraph.

    "Quote Paragraph"

.. pull-quote::

   Pull Quote text 
   
.. highlights::

   Highlights Quote text

.. container:: myclass
   
   Custom Container class.
  
|more| Read more about the :ref:`mastertoc` with a substitution for the image and a link made by a toctree name reference.

This word :term:`Sphinx` with its definition needs to be in the **glossary** or it will rise an error.

.. container:: custom

   This paragraph might be rendered in a custom way.

See :PEP:`287` for more information about reStructuredText. And also a :RFC:`2822` reference for more info about the RFC references.

Modify HTML **metadata** like description and keywords here.

.. meta::
   :description: This HTML document description.
   :keywords: Sphinx, documentation, builder.

Original Text directives were :emphasis:`Emphasis`. :strong:`Strong`. :literal:`Literal`. :subscript:`Subscript`. :superscript:`Superscript`. :title-reference:`Title-Reference`

Area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.

.. math::
   :nowrap:

   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2
   \end{eqnarray}

.. math:: e^{i\pi} + 1 = 0
   :label: euler

Euler's identity, equation :math:numref:`euler`, was elected one of the
most beautiful mathematical formulas.

.. topic:: Topic Title

   Subsequent indented lines comprise
   the body of the topic.

.. versionadded:: 2.5
   For the change log features **added** to the program. 
  
.. versionchanged:: 1.4
   For the change log features **changed** to the program. 

.. deprecated:: 2.5.9
   For the change log features **deprecated** to the program.    
	
.. compound::

   Paragraph 1
      
	  Literal Block.
   
   Paragraph 2
   
Paragraph 1, Literal Block and Paragraph 2 are semantically one compound paragraph.

1. Arabic numerals.

   a) lower alpha
   
      A. upper alpha.
	
* A bullet list

   * Nested bullet list.
   * Nested item 2.
   
      Paragrap 2 of item 2

.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally

.. _sectionTitleRef:

Section Heading Reference
==========================

.. sectionauthor:: Dario Arzaba <darioarzaba@gmail.com>

.. codeauthor:: Dario Arzaba <darioarzaba@gmail.com>

Paragraph with **links**, _`can be standalone hyperlinks` (https://www.google.com , external links `Google_` or some internal cross-reference (sectionTitleRef_) or with custom text like `Custom Title Text <sectionTitleRef_>`_,
external links with custom text like `Google Link <https://www.google.com>`_. Custom text using an external link for the URL is like `Google Link 2 <Google_>_. We can also use internally the ref directive :ref:`sectionTitleRef`.

For **footnotes** and **citations** they can be manual [1]_ , auto-numbered without label [#]_ , with label [#name]_ , or with symbols [*]_ . 
For citations they can be also manual [11]_ or with text [cit1]_. We can replace any text with replace directive like |this|.

We can use section headers as targets like `Section Heading Reference`_. We can also use inline text targets like `can be standalone hyperlinks`_.
An uncommon way of targeting is with anonymous links like `any random text`__.

__ Section Heading Reference_

Link to autodocs class Foo: :class:`test.Foo`.

Here are some auto target footnotes:

.. target-notes::

.. |this| replace:: THIS.

.. _Google: http:google.com

.. rubric:: Footnotes

.. [1] A numbered footnote.
   
   With a second indented paragraph.

.. [#name] A autofootnote using a name.

   Can be referenced using a normal reference or a hyperlink reference.
   
.. [#] An anonymous autofootnote.

.. [*] A symbol footnote.

.. [*] Next symbol footnote etc.

.. [11] This is the citation I made, let's make this extremely long so that we can tell that it doesn't follow the normal responsive table stuff.

.. [cit1] This citation has some meta citation to [13]_ too.

.. [13] This citation is referenced in the previews citation.

Here's the second reference to the above, [cit1]_.

.. |reg| unicode:: U+000AE .. REGISTERED SIGN
   
.. |more| image:: _static/images/more.png
    :height: 16px
    :width: 16px
    :align: middle	
    :alt: more info

Roles
=============================

They are written like:

.. code-block:: rst
   
   :role:`target`

They represent any object in the docs, some create links.

* **any** (:py:mod:`test`) searches with doc, ref, option, extension and intersphinx
* **ref** (:ref:`sectionTitleRef`) use with headers, tables and figures.
* **doc** (:doc:`test`) is used to reference a document.
   * ``:doc:`test``` in a/b/index is a/b/test.
   * ``:doc:`/test``` in a/b/index is a/test.
* **download** (:download:`image <_static/images/something.jpg>`) indicates a document is to be downloaded.
* **numref** (:numref:`Chart of {name} (Fig. {number}) <Fig. 1>`) numbered figure, table or block code.
   * ``numfig=True`` must be set. Optionally ``numfig-format`` and ``numfig_secnum_depth``.
* **envvar** (:envvar:`PATH`) enviroment variable set with an envvar directive.
* **token** (:token:`examplegrammar`) references a token in a productionlist.
* **option** (:option:`secondexecutable -t`) references an option of a command directive.
* **term** (:term:`Sphinx`) references a term in the glossary.
* **math** (:math:`(\pi/4) d^2`) creates inline math.
* **eq** (:eq:`euler`) its the same as math:numref and references a math directive label.
* **menuselection** (:menuselection:`Home --> File --> Some menu`) menu selection sequence.
* **guilabel** (:guilabel:`User action`) references a user action, or a part of the interface,
* **file** (:file:`/usr/lib/python{x}/some`) is a reference to a file or directory.
* **abbr** (:abbr:`LIFO (Last-In, First-Out)`) makes a tooltip for an abbreviation.
* **samp** (:samp:`print 1+{var}`) is a reference to inline code with a custom variable.
* **mimetype** (:mimetype:`text/html`) is a reference to a MIME Type file.
* **manpage** (:manpage:`man.1`) references Unix Manual Page. Manpages_url must be defined.
* **regexp** (:regexp:`2(x|*|-)4`) is a reference to a regex expresion but just in literal.
* **dfn** (:dfn:`important-word`) a term that holds the main idea of a paragraph.
* **kbd** (:kbd:`Control-x Control-f`) keyboard key combination that the user must press.
* **mailheader** (:mailheader:`Message/Partial`) is a reference to a `RFC822_` Mail header.
* **newsgroup** (:newsgroup:`comp.programming`) is a reference to a Usenet newsgroup.
* **command** (:command:`mkdir`) is a reference to an OS level command like mkdir.
* **makevar** (:makevar:`SOMEVAR`) is a reference to a variable for a makefile.
* **program** (:program:`firstexecutable`) is a reference to an executable program.
* **index** (:index:`name`) is a reference to an index entry.

.. _RFC822: https://www.w3.org/Protocols/rfc1341/7_3_Message.html

.. productionlist::
   examplegrammar : "try" ":" `suite`

.. envvar:: PATH

.. program:: firstexecutable

.. option:: -t testArg <optionalTestArg>, --test testArg

   Test Option One Description.

.. program:: secondexecutable

.. option:: -t testArg <optionaltestArg>

   Test Option Two Description.


Term, Options and Fields
===============================

To insert a termin **definition** we indent the definition:

term
    Term definition.

This is an **command options** list:

-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments
-x, -y, -z    Multiple options are an "option group".
-v, --verbose  Commonly-seen: short & long options.
-1 file, --one=file, --two file
              Multiple options with arguments.

To insert a **field list**, we can define any role we desire like author, address, contact, authors, organization, date, status, revision, version, copyright, dedication and abstract:

:Author: David Goodger
:Contact: docutils-develop@lists.sourceforge.net
:Dedication: For Docutils users & co-developers.
:abstract: 

    This document is a demonstration of the reStructuredText markup
    language, containing examples of all basic reStructuredText
    constructs and many advanced constructs.
	
Images and Tables
=======================

Complex Table:

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

Simple Table:

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

Table with a title:

.. table:: Truth table for "not"
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====

CSV Table:

.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy"
   "Gannet Ripple", 1.99, "On a stick!"

List Table:

.. list-table:: List tables can have captions like this one.
    :widths: 10 5 10 50
    :header-rows: 1
    :stub-columns: 1

    * - List table
      - Header 1
      - Header 2
      - Header 3 long. Lorem ipsum dolor sit amet
    * - Stub Row 1
      - Row 1
      - Column 2
      - Column 3 long. Lorem ipsum dolor sit amet
    * - Stub Row 2
      - Row 2
      - Column 2
      - Column 3 long. Lorem ipsum dolor sit amet
    * - Stub Row 3
      - Row 3
      - Column 2
      - Column 3 long. Lorem ipsum dolor sit amet

Images:
        
.. image:: _static/images/something.jpg
   :height: 100px
   :width: 100px
   :align: center
   :target: https://www.google.com
   :alt: Image Alternative Description
   
.. figure:: _static/images/something.jpg
   :figwidth: 200px
   :figclass: align-center
   :name: Fig. 1
   
   Figure Caption
   
   It can also have a figure leyend with anything else.  

.. raw:: html
   
   <iframe width="560" height="315" src="https://www.youtube.com/embed/gHgxFDlXXuU" frameborder="0" allow="accelerometer;s encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

----------------------

Code Blocks
=======================

First Auto Code::

    First Code Block

Second Auto Code ::

    Second Code Block

Sphinx Code Block:

.. code-block:: rest
   :caption: Code Blocks can have captions.
   :linenos:
   :emphasize-lines: 2,4-6,8-
   
   .. toctree::
      :caption: Table of Contents
      :name: mastertoc
      :maxdepth: 2
      :numbered:
      :titlesonly:
      :reversed:
      
      Custom TocTree Title <intro>

Sphinx Code Block Custom Start:

.. code-block:: rest
   :lineno-start: 10

   First code starts at 10
   The next code line

Sphinx Simple Code:

.. code:: bash
   
   Some bash code
   echo 'hello world'

Sphinx Code Block With a name:

.. code-block:: rest
   :caption: this.py
   :name: this-py
   :dedent: 1

     First code line of referenced block.
     The next code line
     This block is also not indented.


Then you can reference this :ref:`This Code Block <this-py>` code block.

Sphinx File Code:

.. literalinclude:: conf.py
   :language: python
   :linenos:
   :lines: 22-24

Doctest Block:

>>> print('this is a Doctest block')
this is a Doctest block
>>> 1 + 1
2

Admonitions
=======================

.. warning::

   Some text for the WARNING.

.. attention::

   Some text for the ATTENTION.

.. caution::

   Some text for the CAUTION.

.. danger::

   Some text for the DANGER
   
.. error::

   Some text for the ERROR.
   
.. hint::

   Some text for the HINT.
   
.. important::

   Some text for the IMPORTANT.
   
.. tip::

   Some text for the TIP.   

.. note::

   Some text for the NOTE.
   
.. seealso::
   
   Module :py:mod:`zipfile`
      For docs on that standard module.
   
   `Other docs link <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_
      This is the docs of the RTD theme.

.. admonition:: And, by the way...

   You can make up your own admonition too.
   