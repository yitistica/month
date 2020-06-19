=============
month package
=============



..  image:: https://img.shields.io/travis/yitistica/month.svg
        :target: https://travis-ci.com/yitistica/month

..
    image:: https://readthedocs.org/projects/month/badge/?version=latest
    :target: https://month.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

About month package:
This is a util package that handles datetime at month level. The package is made up of two modules: *month* and *x_month*.
The *month* module supplies the base classes for manipulating month in a similar fashion as how *datetime* module is built.
The *x_month* module extended the base classes from the *month* module to include additional functionalities.


Installation
------------

.. code-block::

  pip install https://github.com/yitistica/month


Main Features
-------------




Usage
-----
To construct a month object:

.. code-block:: python

   from month.month import Month


License
--------
* Free software: MIT license


Credits
-------

This package shares

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
