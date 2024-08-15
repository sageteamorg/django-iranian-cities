import sys
from typing import Dict

import pytest
from django.db.models import Model

from iranian_cities.models import City, Province, RuralDistrict, Village
from tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.models_code_field,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


class TestCodeField:
    """
    Test suite for verifying the 'code' field of location models.
    """

    def test_province_code(self) -> None:
        """Test the 'code' field of the Province model."""
        province = Province.objects.create(name="Kermanshah", code=19)
        assert province.code == 19

    def test_county_code(self, setup_locations: Dict[str, Model]) -> None:
        """Test the 'code' field of the County model."""
        county = setup_locations["county"]
        assert county.code == 12346

    def test_district_code(self, setup_locations: Dict[str, Model]) -> None:
        """Test the 'code' field of the District model."""
        district = setup_locations["district"]
        assert district.code == 12347

    def test_city_code(self, setup_locations: Dict[str, Model]) -> None:
        """Test the 'code' field of the City model."""
        province = setup_locations["province"]
        county = setup_locations["county"]
        district = setup_locations["district"]
        city = City.objects.create(
            name="Shabad City",
            code=29,
            province=province,
            county=county,
            district=district,
            city_type=1,
        )
        assert city.code == 29

    def test_rural_district_code(self, setup_locations: Dict[str, Model]) -> None:
        """Test the 'code' field of the Rural District model."""
        province = setup_locations["province"]
        county = setup_locations["county"]
        district = setup_locations["district"]
        rural_district = RuralDistrict.objects.create(
            name="Rural District 1",
            code=12349,
            province=province,
            county=county,
            district=district,
        )
        assert rural_district.code == 12349

    def test_village_code(self, setup_locations: Dict[str, Model]) -> None:
        """Test the 'code' field of the Village model."""
        province = setup_locations["province"]
        county = setup_locations["county"]
        district = setup_locations["district"]
        rural_district = RuralDistrict.objects.create(
            name="Rural District 1",
            code=12349,
            province=province,
            county=county,
            district=district,
        )
        village = Village.objects.create(
            name="Black-Black 1",
            code=12350,
            province=province,
            county=county,
            district=district,
            rural_district=rural_district,
            village_type=1,
        )
        assert village.code == 12350
