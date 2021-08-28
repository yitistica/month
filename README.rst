=====
month
=====


.. image:: https://img.shields.io/pypi/v/datetime-month.svg
        :target: https://pypi.python.org/pypi/datetime-month

..  image:: https://github.com/yitistica/month/actions/workflows/pre-release-test.yml/badge.svg
        :target: https://github.com/yitistica/month/actions/workflows/pre-release-test.yml

..  image:: https://readthedocs.org/projects/month/badge/?version=latest
    :target: https://month.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


A package that handles calendar months and arithmetic operation of months.

The package comprises two modules: **month** and **x_month**.
**month** module provides the base classes for manipulating month-level time.
**x_month** module extends the base classes from the *month* module to include additional functionalities.


Installation
------------

.. code-block::

  pip install datetime-month


Features & Usage
----------------

To construct a month object:

.. code-block:: python

   from month import Month
   from month import XMonth  # extended month;

   m = Month(2020, 04)
   xm = Xmonth(2020, 04)

Additional construction methods below can be used to translate a *tuple* (year, month), a *isoformat* string,
an *ordinal* int and *month-format* string into a **Month** object.

.. code-block:: python

   # constructed from a (year, month) tuple:
   m = Month.fromtuple((2019, 11))

   # isoformat is defined as a str in "year-month" format:
   m = Month.fromisoformat('2019-12')

   # ordinal (as in date units):
   m = Month.fromordinal(737390)

   # using string format like datetime:
   m = Month.strptime('2019/1', '%Y/%m')

For the representation of the difference between two months, we can use **Mdelta** (similar to *timedelta* in datetime modules). To construct:

.. code-block:: python

   from month import MDelta
   delta = Mdelta(2)  # Mdelta(months), months: int;

**Mdelta** supports comparisons using operators. It also supports some arithmetic operations (addition, subtraction, and multiplication)
among Mdelta objects or with Month objects or int objects.

.. code-block:: python

   Mdelta(2) < Mdelta(3)  # returns bool;
   Mdelta(2) - Mdelta(3)  # returns Mdelta(-1);
   Mdelta(2) * 2 # returns Mdelta(4);

Some arithmetic operations and comparisons are also supported for **Month** objects.

.. code-block:: python

   Month(2019, 11).add(MDelta(2)) # returns Month(2020, 1);
   Month(2020, 04) + Mdelta(2)  # returns Month(2020, 6);
   Month(2020, 1) - 2  # returns Month(2019, 11);
   Month(2020, 04) <= Month(2020, 06)  # returns True;

**XMonth** is an extended version of **Month** by including some convenient manipulation and sub-level operations.

.. code-block:: python

   xm = XMonth(2019, 11)

   xm.days()  # returns total days in the month;

   xm.first_date()  # returns date(2019,11,1)

   # iterate dates within the month in increment by step days:
   xm.dates(step=2)

   # iterate months in a given range:
   XMonth.range(starting_month, ending_month, step=1)

License
--------
* Free software: MIT license


Credits
-------
This package was created with Cookiecutter_ and `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
