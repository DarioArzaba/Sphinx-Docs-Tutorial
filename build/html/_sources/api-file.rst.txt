
*******************************
An Api Example
*******************************

The default domain is py. To change it we modify ``.. default-domain::``.

For directives and roles of the current domain it is not necessary to write it.
Meaning that ``:py:`` is not necessary as a prefix.

:mod:`MyTestPackage.MyTestModule`
====================================

Another module option is ``deprecated`` to indicate that it is no longer recomended.

.. module:: MyTestPackage.MyTestModule
   :platform: Unix
   :synopsis: This module is a test module for the API page.

.. currentmodule:: MyTestPackage.MyTestModule
   
.. data:: newString
          newString2
		  
Description of the :data:`newString` data and of the other data grouped and how it is used.You cannot use content in modules like :mod:`MyTestPackage.MyTestModule`. To reference an existing module without creating new index entries you can use ``currentmodule``.
 
.. function:: myTestFunction(randomString, [number=1])
      
   .. exception:: OverflowError
	  
   We can reference an exception like this :exc:`OverflowError`.
	  
   Some description of :func:`myTestFunction`, like describing its arguments.
   Functions are module level and generally just contain a field list.
   You can use the ``:async:`` to indicate an async function.
	  
   A field list can use param, parameter, arg, argument, key, keyword, 
   type, raises, raise, except, exception, var, ivar, cvar, vartype, returns, return and rtype.
   
   You can link a type with list(int), dict(str, int), tuple(float, float), int, float, str, None, etc.
   
   :parameter str randomString: Some random string that myTestFunction needs.
   :parameter number: Some number that myTestFunction needs. Can be from 1 to 10.      
   :type number: int or None
   
   :raises OverflowError: If it gets a big number.
   :var: someClassVariable
   :vartype: int (, float)
   :return: The new and better newString.
   :rtype: str
	  
.. function:: compile(source : string, filename, symbol='file') -> ast object

   This function is using Python 3 Style argument annotations.

.. class:: myTestClass (constructorArg)
      
   :param constructorArg: Some information needed for every instance.
	  
   Description of the :class:`myTestClass` with attributes and methods.
	  
   .. attribute:: instanceData
   
      This :attr:`instanceData` is expected to be a string that represents the name of the object. It can be changed directly.
   
   .. attribute:: CONSTANTDATA
   
      A variable that is not intended to be changed can be referenced like :const:`CONSTANTDATA`.
   
   .. method:: testMethod()
   
      Description of this :meth:`testMethod`. Method Options:
 	 
 	  * You can use ``:async:`` to indicate an async method.
 	  * You can use ``:classmethod:`` to indicate a class method.
 	  * You can use ``:property:`` to indicate this is a property method.
 	  * You can use ``:staticmethod:`` to indicate it is a static method.
 	  * You can use ``:abstractmethod:`` to indicate it is an abstract.
      
   .. staticmethod:: testStaticMethod()
      
 	  Description of :meth:`testStaticMethod`
 
   .. classmethod:: testClassMethod()
      
 	  Description of :meth:`testClassMethod`
 	 
   .. decorator:: testDecoratorFunction()
      
 	  Description of :func:`testDecoratorFunction`. Decorator functions modify 
   
   .. decoratormethod:: testDecoratorMethod
 
 	  Description of :meth:`testDecoratorFunction`
 
Extensions
=======================

The ``sphinx-apidoc -o . .`` creates apidoc rst files that pull the api descriptions from the docstrings of the code.

.. code-block:: rest

   .. contents:: Table of Contents

   .. automodule:: test
	  :members:
	  :private-members:
	  :special-members:

Modules must be able to be imported using the path inside ``conf.py``. The new auto directives module, class and exception just output the docstring. 

.. code-block:: rest
   
   .. automodule:: name
   .. autoclass:: name
   .. autoexception:: name
   
If the option ``:members:`` is left empty they generate all members of the class, but you can also target members by a comma separated name list.

.. code-block:: rest
   
   .. automodule:: name
      :members: fooOne, fooTwo
	  
Members without docstrings will be left out unless the option ``:undoc-members:`` is used. Also private members are left out unless ``:private-members:`` option is given. Inherited members are left out unless the ``:members:`` option is empty and the ``:inherited-members:`` option is used. The ``:show-inheritance:`` option inserts a list of inheritance below the class signature. Note that ``automodule`` can use the synopsis, platform and deprecated options in the same way as ``module``. If all but some members are to be documented you can use the empty ``members`` option and then target the exceptions with the ``:exclude-members:``. Content auto directives are:

.. code-block:: rest
   
   .. autofunction:: name
   .. autodecorator:: name
   .. autodata:: name
   .. automethod:: name
   .. autoattribute:: name

Note that ``autodata`` and ``autoattribute`` support the use of the ``:annotation:`` option that overwrites the value shown for the variable. You can add additional comments for every data and attribute by adding ``#: comment`` before or on the variable line.

The ``autosectionlabel`` extension creates labels for every section title of the documentation. 

.. code-block:: rest
   
   A Plain Title
   -------------

   Reference to the title, see :ref:`A Plain Title`.

The ``autosummary`` extension generates a table of functions, methods and attributes.  For example the next code would generate the following summary table:

.. code-block:: rest

   .. autosummary::

      Foo
      Foo.add()

.. currentmodule:: test

.. autosummary::

   Foo
   Foo.add

The ``doctest`` extension tests snippets in the documentation, by searching for doctests tests. The test snippets are divided into *setup code* and *test code*. Test code blocks can be in doctest style (interactive python session) or in code output style (code block and the output). The directives you can use are:

.. code-block:: rest

   .. testsetup:: [group]
   .. testcleanup:: [group]
   .. doctest:: [group]
   .. testcode:: [group]
   .. testoutput:: [group]

The test can be performed with:

.. code-block:: bash

   sphinx-build -b doctest . build
   
Or automatically from the make file:

.. code-block:: bash

   .\make doctest

The following test code imports :file:`test.py` and uses two methods:

.. code-block:: rest

   .. testsetup:: *
      
      import test
      testInstance = test.Foo('hello',spam=False)
   
   .. doctest::
   
      >>> testInstance.add(2, 2)
      4
      
   .. testcode::
   
      r = testInstance.capitalize('testString')
      print(r)
      
   .. testoutput::
   
      TESTSTRING
   
   .. testcleanup::
   
      x = 0

For example

.. testsetup:: *
   
   import test
   testInstance = test.Foo('hello',spam=False)

.. doctest::

   >>> testInstance.add(2, 2)
   4
   
.. testcode::

   r = testInstance.capitalize('testString')
   print(r)
   
.. testoutput::

   TESTSTRING

.. testcleanup::

   x = 0

The ``extlinks`` adds the ``extlinks`` configuration dictionary where you can add links so that you can alias them and reference them quickly. For example:

.. code-block:: rest

   extlinks = {'docs': ('http://example.org/A/%s/+d/index.html', 'framework docs ')}
   
   Example Link: :docs:`1.0.1`,
   Title Example Link: :docs:`documentation (1.2.3) <1.2.3>`.

Example Link: :docs:`1.0.1`,

Title Example Link: :docs:`documentation (1.2.3) <1.2.3>`.

The ``graphviz`` extension allows to embed a Graphviz graph, you can use input code or a dot file.

.. graphviz::
   :align: center
   :caption: Graph caption.
   :name: Graph label.
   
   digraph foo {
      "bar" -> "baz";
   }

.. graphviz::
   :align: center
   :caption: Graph caption.
   :name: Graph label Two.
   
   graph fuzz {
      "bar" -- "baz";
   }

The ``imageconverter`` is just the use of the ``imagemagick`` module to convert images for sphinx when multiple builders are used. The ``viewcode`` adds links to the complete local source code.

The ``intersphinx`` extension creates links between projects using the ``objects.inv`` that is generated for html output. If intersphinx doesnt find a cross reference in the current set it starts searching in the aditional sets configured by the config option ``intersphinx_mapping``, this allows something like :py:class:`zipfile.ZipFile` or :class:`Pets.Pets` to work without having to import the proyect. Another with a reference link would be :py:class:`Pets Example Link <Pets.Pets>`.

The ``todo`` extension adds directives to add reminders of sections that need to be expanded. We can add todo's with:

.. code-block:: rest

   .. todo::
      
	  Create a todo One.
   
   .. todo::
   
      Create a todo Two.
   
   Todo List:
   
   .. todolist::

By default todo's are generated only when ``todo_include_todos`` config option is set to True. If we want them to emit terminal warnings for every Todo we can set to True the ``todo_emit_warnings`` config option.
   
.. todo::
      
   Create a todo One.
   
.. todo::
   
   Create a todo Two.
	
Todo List:
	
.. todolist::

