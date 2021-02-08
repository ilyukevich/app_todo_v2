from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/", views.category, name="category"),
    path("todo/", views.todo, name="todo"),
]