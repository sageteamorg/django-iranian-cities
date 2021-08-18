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
- [Admin](#admin)
- [Git Rules](#git-rules)

## Project Detail

- Language: Python > 3.6
- Framework: Django > 3.1

## Getting Started

First you have to install package using pip:

```shell
$ pip install django-iranian-cities
```

Then you should add `iranian_cities` to INSTALLED_APPS:

```python
INSTALLED_APPS = [
    ...
    'iranian_cities',
    ...
]
```

Now you can migrate to apply model changes:

```shell
$ python manage.py migrate
```

For generating all data you can run this command:

```shell
$ python manage.py generate_city
```

NOTE: you should run this command once (if you want to run again flush db or delete all objects in iranian_cities app)

## Usage

You can use field like this:

```python
from django.db import models
from iranian_cities.fields import OstanField

class TestModel(models.Model):
    ostan = OstanField()
```

list of fields:

- OstanField
- ShahrestanField
- BakhshField
- ShahrField
- DehestanField
- AbadiField


## Admin

You can also use admin mixin class:

```python
from django.contrib import admin
from iranian_cities.admin import IranianCitiesAdmin
from test_app.models import TestModel

@admin.register(TestModel)
class TestModelAdmin(IranianCitiesAdmin):
    pass
```

## Git Rules

S.A.G.E. team Git Rules Policy is available here:

- [S.A.G.E. Git Policy](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

## Team
| [<img src="https://github.com/sageteam-org/django-sage-painless/blob/develop/docs/images/sepehr.jpeg?raw=true" width="230px" height="230px" alt="Sepehr Akbarzadeh">](https://github.com/sepehr-akbarzadeh) | [<img src="https://github.com/sageteam-org/django-sage-painless/blob/develop/docs/images/mehran.png?raw=true" width="225px" height="340px" alt="Mehran Rahmanzadeh">](https://github.com/mehran-rahmanzdeh) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Sepehr Akbarazadeh Maintainer](https://github.com/sepehr-akbarzadeh)                                                                                                             | [Mehran Rahmanzadeh Maintainer](https://github.com/mehran-rahmanzadeh)                                                                                                       |