from django.db import models

from iranian_cities.models import (
    Province, County, District,
    City, RuralDistrict, Village
)


class ProvinceField(models.ForeignKey):
    description = 'Iranian Province'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': Province,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)

class CountyField(models.ForeignKey):
    description = 'Iranian County'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': County,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)

class DistrictField(models.ForeignKey):
    description = 'Iranian District'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': District,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)

class CityField(models.ForeignKey):
    description = 'Iranian City'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': City,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)

class RuralDistrictField(models.ForeignKey):
    description = 'Iranian RuralDistrict'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': RuralDistrict,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)

class VillageField(models.ForeignKey):
    description = 'Iranian Village'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': Village,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)
