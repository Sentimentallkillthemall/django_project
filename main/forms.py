from .models import Vacancy, Summary
from django.forms import ModelForm, TextInput


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ["title","salary","currency","description"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'

            }),
            "salary": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите зарплату'
            }),
            "currency": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите валюту'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            }


class SummaryForm(ModelForm):
    class Meta:
        model = Summary
        fields = ["proffesion", "salary", "currency", "description"]
        widgets = {
            "proffesion": TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Введите название'

            }),
            "salary": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите зарплату'
            }),
            "currency": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите валюту'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
                   }
class FilterVacancy(ModelForm):
    class Meta:
        model = Vacancy
        fields = ["salary"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'

            })
        }


# бд, питоновский кор, http протокол



#не пон как это работает