from django.contrib import admin
from . models import Student

# override the default display on django admin
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","student_number","gender","house","current_class","stream")
    list_filter = ("gender","house","current_class","stream")

# Register your models here.
admin.site.register(Student,StudentAdmin)
