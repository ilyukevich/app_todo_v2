from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Todo
from .models import Category
from django.forms import ModelForm


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name_category', 'description_category', 'slug']
        labels = {
            'name_category': _('Категория'),
            'description_category': _('Описание'),
            'slug': _('Уникальное название'),
        }


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['name_todo', 'category', 'deadline_date', 'description_todo', 'active']
        labels = {
            'name_todo': _('Создайте задание'),
            'category': _('Выберите категорию'),
            'deadline_date': _('Укажите дедлайн (в формате: 03.02.2021 20:43:35)'),
            'description_todo': _('Добавьте комментарий'),
            'active': _('Активно/неактивно'),
        }
