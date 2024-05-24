# тут мы будем регистрировать новые таблицы (или же модели) на страницу администратора
from django.contrib import admin
from .models import Vacancy, Summary



admin.site.register(Vacancy)
admin.site.register(Summary)