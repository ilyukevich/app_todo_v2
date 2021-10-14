from django.db import models
#from django.contrib.auth import get_user_model


class Category(models.Model):
    """***"""

    name_category = models.TextField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description_category = models.TextField('description category', null=True)

    def __str__(self):
        return self.name_category


class Todo(models.Model):
    """***"""

    name_todo = models.TextField('name')
    category = models.ForeignKey(
                                Category,
                                on_delete=models.SET_NULL,
                                null=True, related_name='todo',
                                )
    #pub_date = models.DateTimeField('date published')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    deadline_date = models.DateTimeField('date of deadline')
    description_todo = models.TextField('description todo', null=True)

    class Meta:
        # сортировка дате
        ordering = ["-pub_date"]

    def __str__(self):
        return self.name_todo
