from django.contrib import admin
from django.contrib.admin import widgets
from iranian_cities.models import (
    Province, County, District,
    City, RuralDistrict, Village
)

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
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    search_fields = ['name', 'code']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'province']
    list_filter = ['province']
    search_fields = ['name', 'code', 'province__name']
    raw_id_fields = ['province']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
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

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'county', 'province']
    list_filter = ['province']
    search_fields = ['name', 'code', 'county__name', 'province__name']
    raw_id_fields = ['county', 'province']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(RuralDistrict)
class RuralDistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'district', 'county', 'province']
    list_filter = ['province']
    search_fields = ['name', 'code', 'district__name', 'county__name', 'province__name']
    raw_id_fields = ['district', 'county', 'province']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
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

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
