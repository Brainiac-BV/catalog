from django.contrib import admin
from .models import Book, BookInstance, Author, Genre
# Register your models here.

'''
## standard way of registering models in admin site

admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(Genre)
'''

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance   

# Register model admin class and model w/ admin.
# ModelAdmin allows for better customization of the model class
# This allows for different representations in teh admin backend
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # used to provide filtering options to model fields
    list_filter = ('status', 'due_back')
    # Used to add sections to admin page
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
 

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # below is used to select which fields will show and orientation
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # used for detail view. tuple is for horizontal grouping
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass



