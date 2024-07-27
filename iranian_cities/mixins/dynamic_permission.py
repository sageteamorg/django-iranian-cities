from iranian_cities.conf import sage_iranian_cities_settings

class IranianCitiesAdminReadOnlyEnabled:
    def has_add_permission(self, request):
        return sage_iranian_cities_settings.ADMIN_CAN_ADD

    def has_delete_permission(self, request, obj=None):
        return sage_iranian_cities_settings.ADMIN_CAN_DELETE

    def has_change_permission(self, request, obj=None):
        return sage_iranian_cities_settings.ADMIN_CAN_CHANGE
