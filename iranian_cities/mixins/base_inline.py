from django.contrib import admin


class BaseTabularInline(admin.TabularInline):
    extra = 1
    max_num = 5
