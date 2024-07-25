from django.db import models
from django.utils.translation import gettext_lazy as _
from iranian_cities.mixins import BaseLocation

class Province(BaseLocation):
    """
    Represents a province entity within the application.
    """
    class Meta(BaseLocation.Meta):
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')
        db_table_comment = "Model representing a province."
        db_table = "sage_province"


class County(BaseLocation):
    """
    Represents a county within a province.
    """
    province = models.ForeignKey(
        Province,
        verbose_name=_('Province'),
        related_name='counties',
        help_text=_("The province to which the county belongs."),
        db_comment=_("Foreign key to the Province model."),
        on_delete=models.CASCADE
    )

    class Meta(BaseLocation.Meta):
        verbose_name = _('County')
        verbose_name_plural = _('Counties')
        db_table_comment = "Model representing a county within a province."
        db_table = "sage_county"


class District(BaseLocation):
    """
    Represents a district within a county.
    """
    province = models.ForeignKey(
        Province,
        verbose_name=_('Province'),
        related_name='districts',
        on_delete=models.CASCADE,
        help_text=_("The province to which the district belongs."),
        db_comment=_("Foreign key to the Province model.")
    )
    county = models.ForeignKey(
        County,
        verbose_name=_('County'),
        related_name='districts',
        on_delete=models.CASCADE,
        help_text=_("The county to which the district belongs."),
        db_comment=_("Foreign key to the County model.")
    )

    class Meta(BaseLocation.Meta):
        verbose_name = _('District')
        verbose_name_plural = _('Districts')
        db_table_comment = "Model representing a district within a county."
        db_table = "sage_district"


class City(BaseLocation):
    """
    Represents a city within a district.
    """
    province = models.ForeignKey(
        Province,
        verbose_name=_('Province'),
        related_name='cities',
        on_delete=models.CASCADE,
        help_text=_("The province to which the city belongs."),
        db_comment=_("Foreign key to the Province model.")
    )
    county = models.ForeignKey(
        County,
        verbose_name=_('County'),
        related_name='cities',
        on_delete=models.CASCADE,
        help_text=_("The county to which the city belongs."),
        db_comment=_("Foreign key to the County model.")
    )
    district = models.ForeignKey(
        District,
        verbose_name=_('District'),
        related_name='cities',
        on_delete=models.CASCADE,
        help_text=_("The district to which the city belongs."),
        db_comment=_("Foreign key to the District model.")
    )
    city_type = models.IntegerField(
        verbose_name=_('City Type'),
        help_text=_("The type of city."),
        db_comment=_("Field to define the type of city.")
    )

    class Meta(BaseLocation.Meta):
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        db_table_comment = "Model representing a city within a district."
        db_table = "sage_city"


class RuralDistrict(BaseLocation):
    """
    Represents a rural district within a district.
    """
    province = models.ForeignKey(
        Province,
        verbose_name=_('Province'),
        related_name='rural_districts',
        on_delete=models.CASCADE,
        help_text=_("The province to which the rural district belongs."),
        db_comment=_("Foreign key to the Province model.")
    )
    county = models.ForeignKey(
        County,
        verbose_name=_('County'),
        related_name='rural_districts',
        on_delete=models.CASCADE,
        help_text=_("The county to which the rural district belongs."),
        db_comment=_("Foreign key to the County model.")
    )
    district = models.ForeignKey(
        District,
        verbose_name=_('District'),
        related_name='rural_districts',
        on_delete=models.CASCADE,
        help_text=_("The district to which the rural district belongs."),
        db_comment=_("Foreign key to the District model.")
    )

    class Meta(BaseLocation.Meta):
        verbose_name = _('Rural District')
        verbose_name_plural = _('Rural Districts')
        db_table_comment = "Model representing a rural district within a district."
        db_table = "sage_rural_district"


class Village(BaseLocation):
    """
    Represents a village within a rural district.
    """
    province = models.ForeignKey(
        Province,
        verbose_name=_('Province'),
        related_name='villages',
        on_delete=models.CASCADE,
        help_text=_("The province to which the village belongs."),
        db_comment=_("Foreign key to the Province model.")
    )
    county = models.ForeignKey(
        County,
        verbose_name=_('County'),
        related_name='villages',
        on_delete=models.CASCADE,
        help_text=_("The county to which the village belongs."),
        db_comment=_("Foreign key to the County model.")
    )
    district = models.ForeignKey(
        District,
        verbose_name=_('District'),
        related_name='villages',
        on_delete=models.CASCADE,
        help_text=_("The district to which the village belongs."),
        db_comment=_("Foreign key to the District model.")
    )
    rural_district = models.ForeignKey(
        RuralDistrict,
        verbose_name=_('Rural District'),
        related_name='villages',
        on_delete=models.CASCADE,
        help_text=_("The rural district to which the village belongs."),
        db_comment=_("Foreign key to the Rural District model.")
    )
    village_type = models.IntegerField(
        verbose_name=_('Village Type'),
        help_text=_("The type of village."),
        db_comment=_("Field to define the type of village.")
    )

    class Meta(BaseLocation.Meta):
        verbose_name = _('Village')
        verbose_name_plural = _('Villages')
        db_table_comment = "Model representing a village within a rural district."
        db_table = "sage_village"
