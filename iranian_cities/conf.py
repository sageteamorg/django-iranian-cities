from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from iranian_cities.constants import DEFAULT_SETTINGS

class SageIranianCitiesSettings:
    def __init__(self):
        self._settings = {}
        for setting, default in DEFAULT_SETTINGS.items():
            value = getattr(settings, setting, default)
            if not isinstance(value, bool):
                raise ImproperlyConfigured(
                    f"Setting '{setting}' must be of type boolean."
                )
            self._settings[setting] = value

    def __getattr__(self, item):
        if item in self._settings:
            return self._settings[item]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{item}'"
        )

sage_iranian_cities_settings = SageIranianCitiesSettings()