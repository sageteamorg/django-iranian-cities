import sys
from unittest.mock import MagicMock, patch

import pytest
from django.contrib.admin import AdminSite, widgets
from django.contrib.auth import get_user_model
from django.http import HttpRequest

from iranian_cities.admin import IranianCitiesAdmin
from iranian_cities.models import City, Province
from tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.admin,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]

User = get_user_model()


class TestAdminModel:
    """Class for testing admin models."""

    def test_formfield_for_foreignkey_sets_queryset(self) -> None:
        admin_site: AdminSite = AdminSite()
        request: HttpRequest = HttpRequest()
        request.user = User.objects.create_superuser(
            "Aryan", "aryan@example.com", "password"
        )

        province: Province = Province.objects.create(name="Kermanshah", code=19)

        model_admin: IranianCitiesAdmin = IranianCitiesAdmin(
            model=City, admin_site=admin_site
        )

        db_field = City._meta.get_field("province")

        with patch.object(
            IranianCitiesAdmin,
            "get_field_queryset",
            return_value=Province.objects.filter(name="Kermanshah"),
        ) as mock_get_field_queryset:
            formfield = model_admin.formfield_for_foreignkey(db_field, request)

            mock_get_field_queryset: MagicMock = mock_get_field_queryset
            mock_get_field_queryset.assert_called_once_with(None, db_field, request)

            assert isinstance(formfield.widget, widgets.ForeignKeyRawIdWidget)

            assert list(formfield.queryset) == [province]
