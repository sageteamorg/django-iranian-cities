from typing import Any, Dict

from django.conf import settings

from iranian_cities.constants import DEFAULT_SETTINGS
from iranian_cities.exc import IranianCitiesConfigurationError


class SageIranianCitiesSettings:
    _settings: Dict[str, bool]

    def __init__(self):
        self._settings = {}
        for setting, default in DEFAULT_SETTINGS.items():
            value: Any = getattr(settings, setting, default)
            if not isinstance(value, bool):
                raise IranianCitiesConfigurationError(
                    f"Setting '{setting}' must be of type boolean."
                )
            self._settings[setting] = value

    def __getattr__(self, item: str) -> bool:
        if item in self._settings:
            return self._settings[item]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{item}'"
        )


sage_iranian_cities_settings = SageIranianCitiesSettings()
