import pytest
from typing import Dict
from django.db.models import Model
from tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON
from iranian_cities.models import (
    Province,
    City,
    RuralDistrict,
    Village

)
import sys
pytestmark = [
    pytest.mark.django_db,
    pytest.mark.models_str_method,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON)
]


class TestStrMethod:
    """
    Test suite for verifying the string representation of location models.
    """
    
    def test_province_str(self) -> None:
        """Test the string representation of the Province model."""
        province = Province.objects.create(name="Kermanshah", code=19)
        assert str(province) == "Kermanshah"


    def test_county_str(self, setup_locations: Dict[str, Model]) -> None:
        """Test the string representation of the County model."""
        county = setup_locations['county']
        assert str(county) == "Kermanshah County"


    def test_district_str(self, setup_locations: Dict[str, Model]) -> None:
        """Test the string representation of the District model."""
        district = setup_locations['district']
        assert str(district) == "District 1"


    def test_city_str(self, setup_locations: Dict[str, Model]) -> None:
        """Test the string representation of the City model."""
        province = setup_locations['province']
        county = setup_locations['county']
        district = setup_locations['district']
        city = City.objects.create(name="Shabad City", code=29, province=province, county=county, district=district, city_type=1)
        assert str(city) == "Shabad City"


    def test_rural_district_str(self, setup_locations: Dict[str, Model]) -> None:
        """Test the string representation of the Rural District model."""
        province = setup_locations['province']
        county = setup_locations['county']
        district = setup_locations['district']
        rural_district = RuralDistrict.objects.create(name="Rural District 1", code=12349, province=province, county=county, district=district)
        assert str(rural_district) == "Rural District 1"


    def test_village_str(self, setup_locations: Dict[str, Model]) -> None:
        """Test the string representation of the Village model."""
        province = setup_locations['province']
        county = setup_locations['county']
        district = setup_locations['district']
        rural_district = RuralDistrict.objects.create(name="Rural District 1", code=12349, province=province, county=county, district=district)
        village = Village.objects.create(name="Black-Black 1", code=12350, province=province, county=county, district=district, rural_district=rural_district, village_type=1)
        assert str(village) == "Black-Black 1"
