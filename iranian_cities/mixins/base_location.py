from django.db.models import Model, CharField, BigIntegerField
from django.utils.translation import gettext_lazy as _


class BaseLocation(Model):
    """
    Abstract base model for location entities.

    Attributes:
        name (str): The name of the location.
        code (int): The unique code for the location.
    """
    name = CharField(verbose_name=_("Name"), max_length=255)
    code = BigIntegerField(verbose_name=_("Code"))

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ("id",)
