from django.db import models
from django.utils.translation import gettext_lazy as _


class Province(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    code = models.BigIntegerField(_('Code'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')
        ordering = ('id',)


class County(models.Model):
    province = models.ForeignKey(
        Province,
        verbose_name=_('Province'),
        related_name='county',
        on_delete=models.CASCADE
    )
    name = models.CharField(_('Name'), max_length=255)
    code = models.BigIntegerField(_('Code'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('County')
        verbose_name_plural = _('Counties')
        ordering = ('id',)


class District(models.Model):
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
    name = models.CharField(_('Name'), max_length=255)
    code = models.BigIntegerField(_('Code'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('District')
        verbose_name_plural = _('Districts')
        ordering = ('id',)


class City(models.Model):
    province = models.ForeignKey(
        Province,
        verbose_name=_('province'),
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
    name = models.CharField(_('Name'), max_length=255)
    code = models.BigIntegerField(_('Code'))
    city_type = models.IntegerField(_('City Type'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        ordering = ('id',)


class RuralDistrict(models.Model):
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
    name = models.CharField(_('Name'), max_length=255)
    code = models.BigIntegerField(_('Code'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Rural District')
        verbose_name_plural = _('Rural Districts')
        ordering = ('id',)


class Village(models.Model):
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
    name = models.CharField(_('Name'), max_length=255)
    code = models.BigIntegerField(_('Code'))
    village_type = models.IntegerField(_('Village Type'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Village')
        verbose_name_plural = _('Villages')
        ordering = ('id',)
