from iranian_cities.conf import sage_iranian_cities_settings


class IranianCitiesAdminReadOnlyEnabled:
    def has_add_permission(self, request):
        return (
            not sage_iranian_cities_settings.IRANIAN_CITIES_ADMIN_ADD_READONLY_ENABLED
        )

    def has_delete_permission(self, request, obj=None):
        return (
            not sage_iranian_cities_settings.IRANIAN_CITIES_ADMIN_DELETE_READONLY_ENABLED
        )

    def has_change_permission(self, request, obj=None):
        return (
            not sage_iranian_cities_settings.IRANIAN_CITIES_ADMIN_CHANGE_READONLY_ENABLED
        )


class DynamicInlineAdmin:
    def get_dynamic_inlines(self, model):
        """Returns the list of inlines based on the settings."""
        from iranian_cities.admin import (
            CityInline,
            County,
            CountyInline,
            District,
            DistrictInline,
            Province,
            RuralDistrict,
            VillageInline,
        )

        if sage_iranian_cities_settings.IRANIAN_CITIES_ADMIN_INLINE_ENABLED:
            if model == Province:
                return [CountyInline]
            elif model == County:
                return [DistrictInline]
            elif model == District:
                return [CityInline]
            elif model == RuralDistrict:
                return [VillageInline]
        return []

    def get_inlines(self, request, obj=None):
        return self.get_dynamic_inlines(self.model)
