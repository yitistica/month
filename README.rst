=============
month package
=============



..  image:: https://img.shields.io/travis/yitistica/month.svg
        :target: https://travis-ci.com/yitistica/month

..
    image:: https://readthedocs.org/projects/month/badge/?version=latest
    :target: https://month.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

About
-----
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

   from month import Month
   from month import XMonth  # extended month;

   m = Month(2020, 04)
   xm = Xmonth(2020, 04)

Additional construction methods below can be used to translating a **tuple** (year, month), a **isoformat** string,
an *ordinal** int and **format** string.

.. code-block:: python

   m = Month.fromtuple((2019, 11))  # constructed from a (year, month) tuple;
   m = Month.fromisoformat('2019-12')  # isoformat is defined as a str in "year-month" format;
   m = Month.fromordinal(737390)  # ordinal is supposedly in date unit, we extract its year and month after constructing a datetime.date object.
   m = Month.strptime('2019/1', '%Y/%m')  # using string format like datetime;


For the representation of the difference between two months, we can use *Mdelta* (similar to *timedelta* in datetime modules. For construction

.. code-block:: python

   from month import MDelta
   delta = Mdelta(2)  # Mdelta(months), months: int;

*Mdelta* supports comparisons using operators.
License
--------
* Free software: MIT license


Credits
-------

This package shares

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
