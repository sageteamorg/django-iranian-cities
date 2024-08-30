from typing import Any, Optional

from django.contrib import admin
from django.contrib.admin import widgets
from django.db.models import ForeignKey
from django.http import HttpRequest

from iranian_cities.mixins.base_inline import BaseTabularInline
from iranian_cities.mixins.dynamic_permission import (
    DynamicInlineAdmin,
    IranianCitiesAdminReadOnlyEnabled,
)
from iranian_cities.models import (
    City,
    County,
    District,
    Province,
    RuralDistrict,
    Village,
)


class IranianCitiesAdmin(admin.ModelAdmin):
    """Custom admin model for Iranian cities with a custom form field for
    foreign key."""

    def formfield_for_foreignkey(
        self, db_field: ForeignKey, request: HttpRequest, **kwargs: Any
    ) -> Any:
        """Override the default form field for foreign keys to use
        ForeignKeyRawIdWidget."""
        db: Optional[str] = kwargs.get("using")
        kwargs["widget"] = widgets.ForeignKeyRawIdWidget(
            db_field.remote_field, self.admin_site, using=db
        )

        if "queryset" not in kwargs:
            queryset = self.get_field_queryset(db, db_field, request)
            if queryset is not None:
                kwargs["queryset"] = queryset

        return db_field.formfield(**kwargs)


class CountyInline(BaseTabularInline):
    """Inline admin model for County."""

    model = County
    extra = 1
    raw_id_fields = ["province"]
    max_num = 5


class DistrictInline(BaseTabularInline):
    """Inline admin model for District."""

    model = District
    extra = 1
    raw_id_fields = ["county", "province"]
    max_num = 5


class CityInline(BaseTabularInline):
    """Inline admin model for City."""

    model = City
    extra = 1
    raw_id_fields = ["district", "county", "province"]
    max_num = 5


class RuralDistrictInline(BaseTabularInline):
    """Inline admin model for RuralDistrict."""

    model = RuralDistrict
    extra = 1
    raw_id_fields = ["district", "county", "province"]
    max_num = 5


class VillageInline(BaseTabularInline):
    """Inline admin model for Village."""

    model = Village
    extra = 1
    raw_id_fields = ["rural_district", "district", "county", "province"]
    max_num = 5


@admin.register(Province)
class ProvinceAdmin(
    IranianCitiesAdminReadOnlyEnabled, DynamicInlineAdmin, admin.ModelAdmin
):
    """Admin model for Province."""

    list_display = ["name", "code"]
    search_fields = ["name", "code"]


@admin.register(County)
class CountyAdmin(
    IranianCitiesAdminReadOnlyEnabled, DynamicInlineAdmin, admin.ModelAdmin
):
    """Admin model for County."""

    list_display = ["name", "code", "province"]
    list_filter = ["province"]
    search_fields = ["name", "code", "province__name"]
    raw_id_fields = ["province"]


@admin.register(City)
class CityAdmin(
    IranianCitiesAdminReadOnlyEnabled, DynamicInlineAdmin, admin.ModelAdmin
):
    """Admin model for City."""

    list_display = ["name", "code", "city_type", "district", "county", "province"]
    list_filter = ["province"]
    search_fields = [
        "name",
        "code",
        "city_type",
        "district__name",
        "county__name",
        "province__name",
    ]
    raw_id_fields = ["district", "county", "province"]


@admin.register(District)
class DistrictAdmin(
    IranianCitiesAdminReadOnlyEnabled, DynamicInlineAdmin, admin.ModelAdmin
):
    """Admin model for District."""

    list_display = ["name", "code", "county", "province"]
    list_filter = ["province"]
    search_fields = ["name", "code", "county__name", "province__name"]
    raw_id_fields = ["county", "province"]


@admin.register(RuralDistrict)
class RuralDistrictAdmin(
    IranianCitiesAdminReadOnlyEnabled, DynamicInlineAdmin, admin.ModelAdmin
):
    """Admin model for RuralDistrict."""

    list_display = ["name", "code", "district", "county", "province"]
    list_filter = ["province"]
    search_fields = ["name", "code", "district__name", "county__name", "province__name"]
    raw_id_fields = ["district", "county", "province"]


@admin.register(Village)
class VillageAdmin(
    IranianCitiesAdminReadOnlyEnabled, DynamicInlineAdmin, admin.ModelAdmin
):
    """Admin model for Village."""

    list_display = [
        "name",
        "code",
        "village_type",
        "rural_district",
        "district",
        "county",
        "province",
    ]
    list_filter = ["province"]
    search_fields = [
        "name",
        "code",
        "rural_district__name",
        "district__name",
        "county__name",
        "province__name",
    ]
    raw_id_fields = ["rural_district", "district", "county", "province"]
