from iranian_cities.conf import sage_iranian_cities_settings

class IranianCitiesAdminReadOnlyEnabled:
    def has_add_permission(self, request):
        return sage_iranian_cities_settings.IRANIAN_CITIES_ADMIN_ADD_READONLY_ENABLED

    def has_delete_permission(self, request, obj=None):
        return sage_iranian_cities_settings.IRANIAN_CITIES_ADMIN_DELETE_READONLY_ENABLED

    def has_change_permission(self, request, obj=None):
        return sage_iranian_cities_settings.IRANIAN_CITIES_ADMIN_CHANGE_READONLY_ENABLED
