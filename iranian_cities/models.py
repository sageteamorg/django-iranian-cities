from django.db import models
from django.utils.translation import gettext_lazy as _
from iranian_cities.mixins import BaseLocation

class Province(BaseLocation):
    class Meta(BaseLocation.Meta):
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')


class County(BaseLocation):
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