from typing import Dict

import pytest
from django.db.models import Model

from iranian_cities.models import County, District, Province


@pytest.fixture
def setup_locations() -> Dict[str, Model]:
    province = Province.objects.create(name="Kermanshah", code=12345)
    county = County.objects.create(
        name="Kermanshah County", code=12346, province=province
    )
    district = District.objects.create(
        name="District 1", code=12347, province=province, county=county
    )
    return {"province": province, "county": county, "district": district}
