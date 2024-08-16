# Django Iranian Cities

The [django-iranian-cities](https://github.com/sageteam-org/django-iranian-cities) is a valuable package based on Django Web Framework for Iranian cities support. You can see full documentation here [readthedocs](https://django-iranian-cities.readthedocs.io/).

[![SageTeam](https://github.com/sageteam-org/django-sage-painless/blob/develop/docs/images/tag_sage.png?raw=true "SageTeam")](http://sageteam.org)

![License](https://img.shields.io/github/license/sageteam-org/django-iranian-cities "django-iranian-cities")
![PyPI release](https://img.shields.io/pypi/v/django-iranian-cities "django-iranian-cities")
![Supported Python versions](https://img.shields.io/pypi/pyversions/django-iranian-cities "django-iranian-cities")
![Supported Django versions](https://img.shields.io/pypi/djversions/django-iranian-cities "django-iranian-cities")
![Documentation](https://img.shields.io/readthedocs/django-iranian-cities "django-iranian-cities")
![Last Commit](https://img.shields.io/github/last-commit/sageteam-org/django-iranian-cities/master "django-iranian-cities")
![Languages](https://img.shields.io/github/languages/top/sageteam-org/django-iranian-cities "django-iranian-cities")

- [Project Detail](#project-detail)
- [Get Started](#getting-started)
- [Usage](#usage)
- [Settings](#settings)
- [Git Rules](#git-rules)

## Project Detail

- Language: Python > 3.8
- Framework: Django > 4.2

## Getting Started

1. **Install the package**:

    ```shell
    $ pip install django-iranian-cities
    ```

2. **Add `iranian_cities` to INSTALLED_APPS in your Django settings**:

    ```python
    INSTALLED_APPS = [
        ...
        'iranian_cities',
        ...
    ]
    ```

3. **Run migrations to apply model changes**:

    ```shell
    $ python manage.py migrate
    ```

4. **Generate Data**:
To populate the database with Iranian cities data, use the provided management command. This command will:

   - Check if there is existing data in the tables.
   - Prompt you to confirm if you want to **flush** the tables if they already contain data.
   - Read **CSV** files and populate the `Province`, `County`, `District`, `City`, `RuralDistrict`, and `Village` tables with data.

    ```shell
    $ python manage.py generate_city
    ```
    If **tables** contain data, you will be prompted to either **flush** them or **cancel** the operation.

## Usage

You can use the provided fields and admin mixin in your Django models:

- **Fields**:
    ```python
    from django.db import models
    from iranian_cities.fields import ProvinceField

    class TestModel(models.Model):
        province = ProvinceField()

    ```
    **list of fields**:
    - ProvinceField
    - CountyField
    - DistrictField
    - CityField
    - RuralDistrictField
    - VillageField

- **Admin**:
    ```python
    from django.contrib import admin
    from iranian_cities.admin import IranianCitiesAdmin
    from test_app.models import TestModel

    @admin.register(TestModel)
    class TestModelAdmin(IranianCitiesAdmin):
        pass
    ```

## Settings
The package uses several settings for configuration. Make sure the following settings are defined in your `settings.py` file:
```python
IRANIAN_CITIES_ADMIN_ADD_READONLY_ENABLED = True
IRANIAN_CITIES_ADMIN_DELETE_READONLY_ENABLED = True
IRANIAN_CITIES_ADMIN_CHANGE_READONLY_ENABLED = True
IRANIAN_CITIES_ADMIN_INLINE_ENABLED = False
```
Explanation of **settings**:

- `IRANIAN_CITIES_ADMIN_ADD_READONLY_ENABLED`: When set to `True`, users can add new entries to the admin interface. Set to `False` to disable adding entries.
- `IRANIAN_CITIES_ADMIN_DELETE_READONLY_ENABLED`: When set to `True`, users can delete existing entries in the admin interface. Set to `False` to disable deleting entries.
- `IRANIAN_CITIES_ADMIN_CHANGE_READONLY_ENABLED`: When set to `True`, users can change existing entries in the admin interface. Set to `False` to disable changes.
- `IRANIAN_CITIES_ADMIN_INLINE_ENABLED`: When set to `True`, inline admin forms are enabled based on the model type. Set to `False` to disable inline forms.

![Admin](https://github.com/sageteam-org/django-iranian-cities/blob/master/docs/images/admin.jpg?raw=true)

## Git Rules

S.A.G.E. team Git Rules Policy is available here:

- [S.A.G.E. Git Policy](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
