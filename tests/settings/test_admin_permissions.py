from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.http import HttpRequest
from tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON
from iranian_cities.conf import sage_iranian_cities_settings
from typing import List, Type, Dict, Optional
from iranian_cities.mixins.dynamic_permission import IranianCitiesAdminReadOnlyEnabled, DynamicInlineAdmin
from iranian_cities.admin import (
    Province, County, District, RuralDistrict,
    CityInline, VillageInline, CountyInline, DistrictInline
)
import pytest
import sys


pytestmark = [
    pytest.mark.django_db,
    pytest.mark.settings_admin_permission,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON)
]


class TestAdminPermission:
    """Test IranianCities Admin Permission."""
    def test_iranian_cities_admin_permissions(self) -> None:
        """
        Test the IranianCitiesAdminReadOnlyEnabled mixin to verify that permission
        checks are correctly based on settings.

        This test verifies that add, delete, and change permissions are granted
        or denied based on the configuration settings.

        Returns
        -------
        None
        """
        settings_instance = IranianCitiesAdminReadOnlyEnabled()
        request = HttpRequest()

        # Set configuration settings
        sage_iranian_cities_settings.IRANIAN_CITIES_ADMIN_ADD_READONLY_ENABLED = True
        sage_iranian_cities_settings.IRANIAN_CITIES_ADMIN_DELETE_READONLY_ENABLED = False
        sage_iranian_cities_settings.IRANIAN_CITIES_ADMIN_CHANGE_READONLY_ENABLED = True

        assert settings_instance.has_add_permission(request) is True
        assert settings_instance.has_delete_permission(request) is False
        assert settings_instance.has_change_permission(request) is True

    def test_dynamic_inline_admin(self) -> None:
        """
        Test the DynamicInlineAdmin mixin to ensure that the correct inlines
        are returned based on settings.

        This test checks that the appropriate inline model admins are returned
        for different models when the inline settings are enabled.

        Returns
        -------
        None
        """
        settings_instance = DynamicInlineAdmin()

        # Mock the models and inlines
        sage_iranian_cities_settings.IRANIAN_CITIES_ADMIN_INLINE_ENABLED = True
        
        assert settings_instance.get_dynamic_inlines(Province) == [CountyInline]
        assert settings_instance.get_dynamic_inlines(County) == [DistrictInline]
        assert settings_instance.get_dynamic_inlines(District) == [CityInline]
        assert settings_instance.get_dynamic_inlines(RuralDistrict) == [VillageInline]
        assert settings_instance.get_dynamic_inlines(object) == []

    def test_get_inlines_method(self, settings) -> None:
        """
        Test the `get_inlines` method in a custom admin model admin class.

        This test verifies that the `get_inlines` method returns the correct
        inlines based on the model provided, using the dynamic inline admin settings.

        Parameters
        ----------
        settings : pytest fixture
            The Django settings fixture used to configure the test environment.

        Returns
        -------
        None
        """

        request = HttpRequest()
        request.user = User.objects.create_superuser('admin', 'admin@example.com', 'password')

        class CustomModelAdmin(DynamicInlineAdmin):
            def __init__(self, model: Optional[Type], admin_site: Optional[AdminSite]) -> None:
                self.model = model
                self.admin_site = admin_site

        model_admins: Dict[Type, List[Type]] = {
            Province: [CountyInline],
            County: [DistrictInline],
            District: [CityInline],
            RuralDistrict: [VillageInline]
        }

        for model, expected_inlines in model_admins.items():
            model_admin = CustomModelAdmin(model=model, admin_site=AdminSite())
            
            inlines = model_admin.get_inlines(request)
            
            assert inlines == expected_inlines