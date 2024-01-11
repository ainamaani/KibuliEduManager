from django.contrib import admin
from . models import Book,TakenBook

# override the default display on django admin
class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author","category","isbn")
    list_filter = ("title","category")

class TakenBookAdmin(admin.ModelAdmin):
    list_display = ("book_taken","student_with_book","date_taken","date_returned")
    list_filter = ("status",)

# Register your models here.
admin.site.register(Book,BookAdmin)
admin.site.register(TakenBook,TakenBookAdmin)







