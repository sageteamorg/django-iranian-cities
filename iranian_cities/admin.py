from django.contrib import admin
from django.contrib.admin import widgets
from iranian_cities.models import (
    Province, County, District,
    City, RuralDistrict, Village
)
from iranian_cities.mixins.dynamic_permission import IranianCitiesAdminReadOnlyEnabled

class IranianCitiesAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        db = kwargs.get('using')
        kwargs['widget'] = widgets.ForeignKeyRawIdWidget(
            db_field.remote_field, self.admin_site, using=db)

        if 'queryset' not in kwargs:
            queryset = self.get_field_queryset(db, db_field, request)
            if queryset is not None:
                kwargs['queryset'] = queryset

        return db_field.formfield(**kwargs)

@admin.register(Province)
class ProvinceAdmin(IranianCitiesAdminReadOnlyEnabled, admin.ModelAdmin):
    list_display = ['name', 'code']
    search_fields = ['name', 'code']

@admin.register(County)
class CountyAdmin(IranianCitiesAdminReadOnlyEnabled, admin.ModelAdmin):
    list_display = ['name', 'code', 'province']
    list_filter = ['province']
    search_fields = ['name', 'code', 'province__name']
    raw_id_fields = ['province']

@admin.register(City)
class CityAdmin(IranianCitiesAdminReadOnlyEnabled, admin.ModelAdmin):
    list_display = [
        'name', 'code', 'city_type',
        'district', 'county', 'province'
    ]
    list_filter = ['province']
    search_fields = [
        'name', 'code', 'city_type',
        'district__name', 'county__name', 'province__name'
    ]
    raw_id_fields = ['district', 'county', 'province']

@admin.register(District)
class DistrictAdmin(IranianCitiesAdminReadOnlyEnabled, admin.ModelAdmin):
    list_display = ['name', 'code', 'county', 'province']
    list_filter = ['province']
    search_fields = ['name', 'code', 'county__name', 'province__name']
    raw_id_fields = ['county', 'province']

@admin.register(RuralDistrict)
class RuralDistrictAdmin(IranianCitiesAdminReadOnlyEnabled, admin.ModelAdmin):
    list_display = ['name', 'code', 'district', 'county', 'province']
    list_filter = ['province']
    search_fields = ['name', 'code', 'district__name', 'county__name', 'province__name']
    raw_id_fields = ['district', 'county', 'province']

@admin.register(Village)
class VillageAdmin(IranianCitiesAdminReadOnlyEnabled, admin.ModelAdmin):
    list_display = [
        'name', 'code', 'village_type',
        'rural_district', 'district', 'county', 'province'
    ]
    list_filter = ['province']
    search_fields = [
        'name', 'code', 'rural_district__name',
        'district__name', 'county__name', 'province__name'
    ]
    raw_id_fields = ['rural_district', 'district', 'county', 'province']
