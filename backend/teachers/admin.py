from django.contrib import admin
from . models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','classes_taught')
    list_filter = ('classes_taught','subjects_taught')

# Register your models here.
admin.site.register(Teacher,TeacherAdmin)
