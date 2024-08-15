from typing import Any

from django.db import models

from iranian_cities.models import (
    City,
    County,
    District,
    Province,
    RuralDistrict,
    Village,
)


class ProvinceField(models.ForeignKey):
    """A ForeignKey field for Iranian Provinces."""

    description: str = "Iranian Province"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        defaults = {"to": Province, "on_delete": models.CASCADE}
        defaults.update(kwargs)
        super().__init__(*args, **defaults)


class CountyField(models.ForeignKey):
    """A ForeignKey field for Iranian Counties."""

    description: str = "Iranian County"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        defaults = {"to": County, "on_delete": models.CASCADE}
        defaults.update(kwargs)
        super().__init__(*args, **defaults)


class DistrictField(models.ForeignKey):
    """A ForeignKey field for Iranian Districts."""

    description: str = "Iranian District"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        defaults = {"to": District, "on_delete": models.CASCADE}
        defaults.update(kwargs)
        super().__init__(*args, **defaults)


class CityField(models.ForeignKey):
    """A ForeignKey field for Iranian Cities."""

    description: str = "Iranian City"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        defaults = {"to": City, "on_delete": models.CASCADE}
        defaults.update(kwargs)
        super().__init__(*args, **defaults)


class RuralDistrictField(models.ForeignKey):
    """A ForeignKey field for Iranian Rural Districts."""

    description: str = "Iranian Rural District"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        defaults = {"to": RuralDistrict, "on_delete": models.CASCADE}
        defaults.update(kwargs)
        super().__init__(*args, **defaults)


class VillageField(models.ForeignKey):
    """A ForeignKey field for Iranian Villages."""

    description: str = "Iranian Village"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        defaults = {"to": Village, "on_delete": models.CASCADE}
        defaults.update(kwargs)
        super().__init__(*args, **defaults)
