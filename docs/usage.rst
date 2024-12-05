Usage
=====

You can use the provided fields and admin mixin in your Django models:

- **Fields**:

    .. code-block:: python

        from django.db import models
        from iranian_cities.fields import ProvinceField


        class TestModel(models.Model):
            province = ProvinceField()

    **List of fields**:
    - `ProvinceField`
    - `CountyField`
    - `DistrictField`
    - `CityField`
    - `RuralDistrictField`
    - `VillageField`

- **Admin**:

    .. code-block:: python

        from django.contrib import admin
        from iranian_cities.admin import IranianCitiesAdmin
        from test_app.models import TestModel


        @admin.register(TestModel)
        class TestModelAdmin(IranianCitiesAdmin):
            pass
