from django.contrib import admin
from .models import Book, BookNumber


# admin.site.register(Book) # this allows book to show up on the admin page
# Register your models here.
@admin.register(Book)
class BookAdmin(
    admin.ModelAdmin):  # what this is saying is we still register our book to the admin site so we can also use ut
    # fields = ['title', 'description'] # this restricts what is displayed on admin page
    list_display = ['title', 'description',
                    'price']  # this makes the table actually display what is in each book object like excel
    list_filter = ['published']
    search_fields = ['title']


admin.site.register(BookNumber)

# @admin.register(BookNumber)
# class BookAdmin(admin.ModelAdmin): # what this is saying is we still register our book to the admin site so we can also use ut
#     # fields = ['title', 'description'] # this restricts what is displayed on admin page
#     list_display = ['isbn_10', 'isbn_13'] # this makes the table actually display what is in each book object like excel
