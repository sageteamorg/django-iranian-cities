from django.db.models import BigIntegerField, CharField, Index, Model
from django.utils.translation import gettext_lazy as _


class BaseLocation(Model):
    """Abstract base model for location entities."""

    name = CharField(
        verbose_name=_("Name"),
        max_length=255,
        help_text=_("The name of the location."),
        db_comment="This field stores the name of the location.",
    )
    code = BigIntegerField(
        verbose_name=_("Code"),
        help_text=_("The code representing the location."),
        db_comment="This field stores the code for the location.",
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ["id"]
        indexes = [
            Index(fields=["code"]),
        ]
