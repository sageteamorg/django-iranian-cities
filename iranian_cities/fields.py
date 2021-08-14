from django.db import models
from django import forms

from iranian_cities.models import (
    Ostan, Shahrestan, Bakhsh,
    Shahr, Dehestan, Abadi
)


class OstanField(models.ForeignKey):
    description = 'Iranian Ostan'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': Ostan,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)

class ShahrestanField(models.ForeignKey):
    description = 'Iranian Shahrestan'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': Shahrestan,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)

class BakhshField(models.ForeignKey):
    description = 'Iranian Bakhsh'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': Bakhsh,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)

class ShahrField(models.ForeignKey):
    description = 'Iranian Shahr'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': Shahr,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)

class DehestanField(models.ForeignKey):
    description = 'Iranian Dehestan'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': Dehestan,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)

class AbadiField(models.ForeignKey):
    description = 'Iranian Abadi'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': Abadi,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)
