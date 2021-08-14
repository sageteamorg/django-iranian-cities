from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ostan(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    amar_code = models.IntegerField(_('Amar Code'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Ostan')
        verbose_name_plural = _('Ostans')
        ordering = ('id',)


class Shahrestan(models.Model):
    ostan = models.ForeignKey(
        Ostan,
        verbose_name=_('Ostan'),
        related_name='shahrestans',
        on_delete=models.CASCADE
    )
    name = models.CharField(_('Name'), max_length=255)
    amar_code = models.IntegerField(_('Amar Code'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Shahrestan')
        verbose_name_plural = _('Shahrestans')
        ordering = ('id',)


class Bakhsh(models.Model):
    ostan = models.ForeignKey(
        Ostan,
        verbose_name=_('Ostan'),
        related_name='bakhshs',
        on_delete=models.CASCADE
    )
    shahrestan = models.ForeignKey(
        Shahrestan,
        verbose_name=_('Shahrestan'),
        related_name='bakhshs',
        on_delete=models.CASCADE
    )
    name = models.CharField(_('Name'), max_length=255)
    amar_code = models.IntegerField(_('Amar Code'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Bakhsh')
        verbose_name_plural = _('Bakhshs')
        ordering = ('id',)


class Shahr(models.Model):
    ostan = models.ForeignKey(
        Ostan,
        verbose_name=_('Ostan'),
        related_name='shahrs',
        on_delete=models.CASCADE
    )
    shahrestan = models.ForeignKey(
        Shahrestan,
        verbose_name=_('Shahrestan'),
        related_name='shahrs',
        on_delete=models.CASCADE
    )
    bakhsh = models.ForeignKey(
        Bakhsh,
        verbose_name=_('Bakhsh'),
        related_name='shahrs',
        on_delete=models.CASCADE
    )
    name = models.CharField(_('Name'), max_length=255)
    amar_code = models.IntegerField(_('Amar Code'))
    shahr_type = models.IntegerField(_('Shahr Type'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Shahr')
        verbose_name_plural = _('Shahrs')
        ordering = ('id',)


class Dehestan(models.Model):
    ostan = models.ForeignKey(
        Ostan,
        verbose_name=_('Ostan'),
        related_name='dehestans',
        on_delete=models.CASCADE
    )
    shahrestan = models.ForeignKey(
        Shahrestan,
        verbose_name=_('Shahrestan'),
        related_name='dehestans',
        on_delete=models.CASCADE
    )
    bakhsh = models.ForeignKey(
        Bakhsh,
        verbose_name=_('Bakhsh'),
        related_name='dehestans',
        on_delete=models.CASCADE
    )
    name = models.CharField(_('Name'), max_length=255)
    amar_code = models.IntegerField(_('Amar Code'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Dehestan')
        verbose_name_plural = _('Dehestans')
        ordering = ('id',)


class Abadi(models.Model):
    ostan = models.ForeignKey(
        Ostan,
        verbose_name=_('Ostan'),
        related_name='abadies',
        on_delete=models.CASCADE
    )
    shahrestan = models.ForeignKey(
        Shahrestan,
        verbose_name=_('Shahrestan'),
        related_name='abadies',
        on_delete=models.CASCADE
    )
    bakhsh = models.ForeignKey(
        Bakhsh,
        verbose_name=_('Bakhsh'),
        related_name='abadies',
        on_delete=models.CASCADE
    )
    dehestan = models.ForeignKey(
        Dehestan,
        verbose_name=_('Dehestan'),
        related_name='abadies',
        on_delete=models.CASCADE
    )
    name = models.CharField(_('Name'), max_length=255)
    amar_code = models.IntegerField(_('Amar Code'))
    abadi_type = models.IntegerField(_('Abadi Type'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Abadi')
        verbose_name_plural = _('Abadies')
        ordering = ('id',)
