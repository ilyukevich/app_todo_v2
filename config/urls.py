from django.contrib import admin
from django.urls import include, path


urlpatterns = [

    # раздел администратора
    path("admin/", admin.site.urls),
    # обработчик для главной страницы ищем в urls.py приложения todolist
    path("", include("apps.todolist.urls")),

]
