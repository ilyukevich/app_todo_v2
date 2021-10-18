from django.contrib import admin
from .models import Todo, Category


class CategoryAdmin(admin.ModelAdmin):
    """fields that should be displayed in the admin panel"""

    list_display = ('name_category', 'slug', 'description_category')
    search_fields = ('name_category',)
    list_filter = ('name_category',)
    empty_value_display = '-пусто-'


class TodoAdmin(admin.ModelAdmin):
    """Group fields that are displayed in the admin panel"""
    list_display = ('name_todo', 'category', 'pub_date', 'upd_date', 'deadline_date', 'description_todo', 'active')
    search_fields = ('name_todo',)
    list_filter = ('pub_date', 'upd_date', 'deadline_date',)
    empty_value_display = '-пусто-'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Todo, TodoAdmin)
