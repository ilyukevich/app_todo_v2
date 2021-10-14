from django.contrib import admin
from .models import Todo, Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    """fields that should be displayed in the admin panel"""
    # add column 'pk' to the beginning
    list_display = ('name_category', 'slug', 'description_category')
    # adding an interface for searching by post text
    search_fields = ('name_category',)
    # adding the ability to filter by date
    list_filter = ('name_category',)
    empty_value_display = '-пусто-'


class TodoAdmin(admin.ModelAdmin):
    """Group fields that are displayed in the admin panel"""
    list_display = ('name_todo', 'category', 'pub_date', 'deadline_date', 'description_todo')
    search_fields = ()
    list_filter = ()
    empty_value_display = '-пусто-'


# when registering a Post model as a configuration source, assign the PostAdmin class to it
admin.site.register(Category, CategoryAdmin)
admin.site.register(Todo, TodoAdmin)
