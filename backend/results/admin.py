from django.contrib import admin
from . models import Result

# Register your models here.

class ResultAdmin(admin.ModelAdmin):
    list_display = ('student','term','subject')
    list_filter = ('student','term','grades','subject')

admin.register(Result,ResultAdmin)
    
