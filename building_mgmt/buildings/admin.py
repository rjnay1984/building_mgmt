from django.contrib import admin
from .models import Building, Unit

# Register your models here.


class UnitInline(admin.TabularInline):
    model = Unit


class BuildingAdmin(admin.ModelAdmin):
    list_display = ['address', 'city', 'landlord']
    ordering = ['address', 'city', 'landlord']
    inlines = [UnitInline]


admin.site.register(Building, BuildingAdmin)
admin.site.register(Unit)
