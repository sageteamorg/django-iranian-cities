from typing import List
from iranian_cities.checks import check_iranian_cities_config
from iranian_cities.exc import IranianCitiesConfigurationError
from iranian_cities.conf import SageIranianCitiesSettings
from tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON
import pytest
import sys

pytestmark = [
    pytest.mark.settings_checks,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON)
]

class TestIranianCitiesConfig:
    """Test IranianCities configuration and settings."""
    def test_check_iranian_cities_config_correct_settings(self, settings) -> None:
        """
        Test the Iranian Cities configuration checker with correct settings.

        This test verifies that no errors are returned when all required settings
        are correctly configured.

        Parameters
        ----------
        settings : pytest.Settings
            The Django settings fixture used to configure the test environment.
        """
        settings.IRANIAN_CITIES_ADMIN_ADD_READONLY_ENABLED = True
        settings.IRANIAN_CITIES_ADMIN_DELETE_READONLY_ENABLED = True
        settings.IRANIAN_CITIES_ADMIN_CHANGE_READONLY_ENABLED = True
        settings.IRANIAN_CITIES_ADMIN_INLINE_ENABLED = True

        errors: List[Exception] = check_iranian_cities_config({})
        assert len(errors) == 0

    def test_sage_iranian_cities_settings(self, settings) -> None:
        """
        Test the SageIranianCitiesSettings class with correct settings.

        This test verifies that the settings class reads and applies the correct
        settings values.

        Parameters
        ----------
        settings : pytest.Settings
            The Django settings fixture used to configure the test environment.
        """
        settings.IRANIAN_CITIES_ADMIN_ADD_READONLY_ENABLED = True
        settings.IRANIAN_CITIES_ADMIN_DELETE_READONLY_ENABLED = True
        settings.IRANIAN_CITIES_ADMIN_CHANGE_READONLY_ENABLED = True
        settings.IRANIAN_CITIES_ADMIN_INLINE_ENABLED = True

        settings_instance = SageIranianCitiesSettings()

        assert settings_instance.IRANIAN_CITIES_ADMIN_ADD_READONLY_ENABLED is True
        assert settings_instance.IRANIAN_CITIES_ADMIN_DELETE_READONLY_ENABLED is True
        assert settings_instance.IRANIAN_CITIES_ADMIN_CHANGE_READONLY_ENABLED is True
        assert settings_instance.IRANIAN_CITIES_ADMIN_INLINE_ENABLED is True

    def test_check_iranian_cities_config_invalid_type_again(self, settings) -> None:
        """
        Test the Iranian Cities configuration checker with invalid type settings.

        This test ensures that an IranianCitiesConfigurationError is raised when
        settings are of the wrong type.

        Parameters
        ----------
        settings : pytest.Settings
            The Django settings fixture used to configure the test environment.
        """
        settings.IRANIAN_CITIES_ADMIN_ADD_READONLY_ENABLED = "true"
        settings.IRANIAN_CITIES_ADMIN_DELETE_READONLY_ENABLED = True
        settings.IRANIAN_CITIES_ADMIN_CHANGE_READONLY_ENABLED = True
        settings.IRANIAN_CITIES_ADMIN_INLINE_ENABLED = True

        with pytest.raises(IranianCitiesConfigurationError):
            SageIranianCitiesSettings()

    def test_sage_iranian_cities_settings_missing_configs(self, settings) -> None:
        """
        Test the SageIranianCitiesSettings class with missing configuration values.

        This test verifies that an IranianCitiesConfigurationError is raised when
        required settings are missing or set to None.

        Parameters
        ----------
        settings : pytest.Settings
            The Django settings fixture used to configure the test environment.
        """
        settings.IRANIAN_CITIES_ADMIN_ADD_READONLY_ENABLED = None
        settings.IRANIAN_CITIES_ADMIN_DELETE_READONLY_ENABLED = None
        settings.IRANIAN_CITIES_ADMIN_CHANGE_READONLY_ENABLED = None
        settings.IRANIAN_CITIES_ADMIN_INLINE_ENABLED = None

        with pytest.raises(IranianCitiesConfigurationError) as excinfo:
            SageIranianCitiesSettings()

        error_message: str = str(excinfo.value)

        assert excinfo.value.code == "E4001"  
        assert excinfo.value.section_code == "CFG" 

        assert "must be of type boolean" in error_message