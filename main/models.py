# Модель это грубо говоря таблица, (то есть база данных)
from django.db import models
from django.contrib.auth.models import User

class Vacancy(models.Model):
    title = models.CharField('Вакансия', max_length=100) # charfield - до 255 символов
    salary = models.DecimalField('Зарплата', max_digits=10, decimal_places=2, null=True)
    currency = models.CharField('Валюта',max_length=5, null=True)
    description = models.TextField('Описание')# textfield - чето побольше

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.title

class Summary(models.Model):
    proffesion = models.CharField('Проффесия', max_length=50)
    salary = models.DecimalField('Зарплата', max_digits=10, decimal_places=2, null=True)
    currency = models.CharField('Валюта', max_length=5, null=True)
    description = models.TextField('Описание')

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.proffesion} {self.author.username}"
    # не пон