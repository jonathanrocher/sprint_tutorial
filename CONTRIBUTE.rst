
To contribute to this project, you need to make sure that:

    * your code is pep8 compliant,
    * your code has been run through pyflakes,
    * the test suite passes,
    * the documentation builds.


Guidelines for contributors
===========================
To learn to contribute to projects, please refer to the
``doc/how_to_sprint.rst`` documentation file.


Test suite
==========
The test suite is run using ``nosetests``::

    $ nosetests -v sprint_tutorial


Documentation
=============
The documentation, in the ``doc/`` folder, must be built using sphinx::

    $ cd doc
    $ make html

