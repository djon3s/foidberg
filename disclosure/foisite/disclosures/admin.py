from django.contrib import admin
from disclosures.models import Department, DjangoDisclosure
"""can revist this later at the tutorial
class DepartmentAdmin(admin.ModelAdmin):
    fields = ['url','name']

class DjangoDisclosureAdmin(admin.ModelAdmin):
"""
admin.site.register(Department)
admin.site.register(DjangoDisclosure)

