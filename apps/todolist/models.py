from django.db import models
#from django.contrib.auth import get_user_model


class Category(models.Model):
    """Модель для категории"""

    name_category = models.TextField('name category', max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description_category = models.TextField('description category', null=True)

    def __str__(self):
        return self.name_category


class Todo(models.Model):
    """Модель для карточки задания"""

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='todo',)
    name_todo = models.TextField('name todo')
    description_todo = models.TextField('description todo', null=True)
    pub_date = models.DateTimeField('date created todo', auto_now_add=True)
    deadline_date = models.DateTimeField('date of deadline todo')
    upd_date = models.DateTimeField('date update todo', auto_now=True)
    active = models.BooleanField('active', default=True)


    class Meta:

        ordering = ["-pub_date"]

    def __str__(self):
        return self.name_todo
