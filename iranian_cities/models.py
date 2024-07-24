from django.db import models
from django.utils.translation import gettext_lazy as _
from iranian_cities.mixins import BaseLocation

class Province(BaseLocation):
    """
    Model representing a province.

    Inherits from BaseLocation.
    """
    class Meta(BaseLocation.Meta):
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')


class County(BaseLocation):
    """
    Model representing a county.

    Attributes:
        province (ForeignKey): The province to which the county belongs.
    """
    province = models.ForeignKey(
        Province,
        verbose_name=_('Province'),
        related_name='counties',
        on_delete=models.CASCADE
    )

    class Meta(BaseLocation.Meta):
        verbose_name = _('County')
        verbose_name_plural = _('Counties')


class District(BaseLocation):
    """
    Model representing a district.

    Attributes:
        province (ForeignKey): The province to which the district belongs.
        county (ForeignKey): The county to which the district belongs.
    """
    province = models.ForeignKey(
        Province,
        verbose_name=_('Province'),
        related_name='districts',
        on_delete=models.CASCADE
    )
    county = models.ForeignKey(
        County,
        verbose_name=_('County'),
        related_name='districts',
        on_delete=models.CASCADE
    )

    class Meta(BaseLocation.Meta):
        verbose_name = _('District')
        verbose_name_plural = _('Districts')


class City(BaseLocation):
    """
    Model representing a city.

    Attributes:
        province (ForeignKey): The province to which the city belongs.
        county (ForeignKey): The county to which the city belongs.
        district (ForeignKey): The district to which the city belongs.
        city_type (int): The type/category of the city.
    """
    province = models.ForeignKey(
        Province,
        verbose_name=_('Province'),
        related_name='cities',
        on_delete=models.CASCADE
    )
    county = models.ForeignKey(
        County,
        verbose_name=_('County'),
        related_name='cities',
        on_delete=models.CASCADE
    )
    district = models.ForeignKey(
        District,
        verbose_name=_('District'),
        related_name='cities',
        on_delete=models.CASCADE
    )
    city_type = models.IntegerField(_('City Type'))

    class Meta(BaseLocation.Meta):
        verbose_name = _('City')
        verbose_name_plural = _('Cities')


class RuralDistrict(BaseLocation):
    """
    Model representing a rural district.

    Attributes:
        province (ForeignKey): The province to which the rural district belongs.
        county (ForeignKey): The county to which the rural district belongs.
        district (ForeignKey): The district to which the rural district belongs.
    """
    province = models.ForeignKey(
        Province,
        verbose_name=_('Province'),
        related_name='ruraldistricts',
        on_delete=models.CASCADE
    )
    county = models.ForeignKey(
        County,
        verbose_name=_('County'),
        related_name='ruraldistricts',
        on_delete=models.CASCADE
    )
    district = models.ForeignKey(
        District,
        verbose_name=_('District'),
        related_name='ruraldistricts',
        on_delete=models.CASCADE
    )

    class Meta(BaseLocation.Meta):
        verbose_name = _('Rural District')
        verbose_name_plural = _('Rural Districts')


class Village(BaseLocation):
    """
    Model representing a village.

    Attributes:
        province (ForeignKey): The province to which the village belongs.
        county (ForeignKey): The county to which the village belongs.
        district (ForeignKey): The district to which the village belongs.
        rural_district (ForeignKey): The rural district to which the village belongs.
        village_type (int): The type/category of the village.
    """
    province = models.ForeignKey(
        Province,
        verbose_name=_('Province'),
        related_name='villages',
        on_delete=models.CASCADE
    )
    county = models.ForeignKey(
        County,
        verbose_name=_('County'),
        related_name='villages',
        on_delete=models.CASCADE
    )
    district = models.ForeignKey(
        District,
        verbose_name=_('District'),
        related_name='villages',
        on_delete=models.CASCADE
    )
    rural_district = models.ForeignKey(
        RuralDistrict,
        verbose_name=_('Rural District'),
        related_name='villages',
        on_delete=models.CASCADE
    )
    village_type = models.IntegerField(_('Village Type'))

    class Meta(BaseLocation.Meta):
        verbose_name = _('Village')
        verbose_name_plural = _('Villages')