from django.contrib import admin
from . models import Subject

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name','code','class_level','teacher')
    list_filter = ('class','teacher')