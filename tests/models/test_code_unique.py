import sys
from typing import Dict

import pytest
from django.db import IntegrityError
from django.db.models import Model

from iranian_cities.models import (
    City,
    County,
    District,
    Province,
    RuralDistrict,
    Village,
)
from tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.models_code_field_unique,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


class TestCodeFieldUnique:
    """
    Test suite for ensuring uniqueness constraints on the 'code' fields
    for various location models.
    """

    def test_province_code_unique(self) -> None:
        """Test that duplicate 'code' values are not allowed for Province."""
        Province.objects.create(name="Kermanshah", code=19)
        with pytest.raises(IntegrityError):
            Province.objects.create(name="Tehran", code=19)

    def test_county_code_unique(self, setup_locations: Dict[str, Model]) -> None:
        """Test that duplicate 'code' values are not allowed for County."""
        County.objects.create(
            name="Another County", code=12348, province=setup_locations["province"]
        )
        with pytest.raises(IntegrityError):
            County.objects.create(
                name="Duplicate County",
                code=12348,
                province=setup_locations["province"],
            )

    def test_district_code_unique(self, setup_locations: Dict[str, Model]) -> None:
        """Test that duplicate 'code' values are not allowed for District."""
        District.objects.create(
            name="Another District",
            code=12348,
            province=setup_locations["province"],
            county=setup_locations["county"],
        )
        with pytest.raises(IntegrityError):
            District.objects.create(
                name="Duplicate District",
                code=12348,
                province=setup_locations["province"],
                county=setup_locations["county"],
            )

    def test_city_code_unique(self, setup_locations: Dict[str, Model]) -> None:
        """Test that duplicate 'code' values are not allowed for City."""
        City.objects.create(
            name="Another City",
            code=29,
            province=setup_locations["province"],
            county=setup_locations["county"],
            district=setup_locations["district"],
            city_type=1,
        )
        with pytest.raises(IntegrityError):
            City.objects.create(
                name="Duplicate City",
                code=29,
                province=setup_locations["province"],
                county=setup_locations["county"],
                district=setup_locations["district"],
                city_type=1,
            )

    def test_rural_district_code_unique(
        self, setup_locations: Dict[str, Model]
    ) -> None:
        """Test that duplicate 'code' values are not allowed for Rural District."""
        RuralDistrict.objects.create(
            name="Another Rural District",
            code=12348,
            province=setup_locations["province"],
            county=setup_locations["county"],
            district=setup_locations["district"],
        )
        with pytest.raises(IntegrityError):
            RuralDistrict.objects.create(
                name="Duplicate Rural District",
                code=12348,
                province=setup_locations["province"],
                county=setup_locations["county"],
                district=setup_locations["district"],
            )

    def test_village_code_unique(self, setup_locations: Dict[str, Model]) -> None:
        """Test that duplicate 'code' values are not allowed for Village."""
        rural_district = RuralDistrict.objects.create(
            name="Another Rural District",
            code=12348,
            province=setup_locations["province"],
            county=setup_locations["county"],
            district=setup_locations["district"],
        )
        Village.objects.create(
            name="Another Village",
            code=12350,
            province=setup_locations["province"],
            county=setup_locations["county"],
            district=setup_locations["district"],
            rural_district=rural_district,
            village_type=1,
        )
        with pytest.raises(IntegrityError):
            Village.objects.create(
                name="Duplicate Village",
                code=12350,
                province=setup_locations["province"],
                county=setup_locations["county"],
                district=setup_locations["district"],
                rural_district=rural_district,
                village_type=1,
            )
