from django.contrib import admin
from . models import Application

# override the default display on django admin
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","current_class","class_applied_for")
    list_filter = ("current_class","class_applied_for")

# Register your models here.
admin.site.register(Application,ApplicationAdmin)
