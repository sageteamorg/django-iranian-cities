from django.contrib import admin


class BaseTabularInline(admin.TabularInline):
    """Base class for inline models using a tabular layout."""

    extra = 1
    max_num = 5
