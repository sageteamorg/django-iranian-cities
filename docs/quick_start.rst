Quick Start
===========

Getting Started
---------------

First you have to install package using pip:

.. code:: shell

    $ pip install django-iranian-cities

Then you should add `iranian_cities` to INSTALLED_APPS:

.. code:: python

    INSTALLED_APPS = [
    ...
    'iranian_cities',
    ...
    ]

Now you can migrate to apply model changes:

.. code:: shell

    $ python manage.py migrate

For generating all data you can run this command:

.. code:: shell

    $ python manage.py generate_city

NOTE: you should run this command once (if you want to run again flush db or delete all objects in iranian_cities app)
