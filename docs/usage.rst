Usage
=====

Field
-----

You can use field like this:

.. code:: python

    from django.db import models
    from iranian_cities.fields import OstanField

    class TestModel(models.Model):
        ostan = OstanField()

list of fields:

- OstanField
- ShahrestanField
- BakhshField
- ShahrField
- DehestanField
- AbadiField

Admin
-----

You can also use admin mixin class:

.. code:: python

    from django.contrib import admin
    from iranian_cities.admin import IranianCitiesAdmin
    from test_app.models import TestModel

    @admin.register(TestModel)
    class TestModelAdmin(IranianCitiesAdmin):
        pass