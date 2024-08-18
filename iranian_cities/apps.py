from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class IranianCitiesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "iranian_cities"
    verbose_name = _("Iranian Cities")

    def ready(self) -> None:
        from . import checks
