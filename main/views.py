# ТУТ МЫ БУДЕМ ПОКАЗЫВАТЬ КАКОЙ ЛИБО HTML ШАБЛОН ПРИ ПЕРЕХОДЕ НА НОВУЮ СТРАНИЦУ (ЕСЛИ ПОЛЬЗОВАТЕЛЬ ПЕРЕШЕЛ НА ГЛАУНЮ СТРАНИЦУ ТО МЫ ПОКАЖЕМ ЕМУ ТАКОЙ ТО ШАБЛОН)
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Vacancy, Summary
from .forms import SummaryForm, VacancyForm, FilterVacancy

def index(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'main/index.html', {'title': 'Вакансии', 'vacancies': vacancies})

def about_us(request):
    return render(request, 'main/about_us.html')

def update_vacancy(request, vacancy_id):
    error = ''
    vacancy_to_edit = Vacancy.objects.get(id=vacancy_id)
    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=vacancy_to_edit)
        if vacancy_to_edit.author and request.user.id == vacancy_to_edit.author.id:
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('home')
            else:
                error = 'Форма была неверной'
        else:
            error = 'Вы не можете изменить эту вакансию, так как вы не её автор'
    else:
        form = VacancyForm(instance=vacancy_to_edit)
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/update_vacancy.html', context)
def update_summary(request, summary_id):
    error = ''
    summary_to_edit = Summary.objects.get(id=summary_id)
    if request.method == 'POST':
        form = SummaryForm(request.POST, instance=summary_to_edit)
        if summary_to_edit.author and request.user.id == summary_to_edit.author.id:
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('home')
            else:
                error = 'Форма была неверной'
        else:
            error = 'Вы не можете изменить это резюме, так как вы не её автор'
    else:
        form = SummaryForm(instance=summary_to_edit)
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/update_summary.html', context)


def delete_vacancy(requset, vacancy_id):
    vacancy_to_delete = Vacancy.objects.get(id=vacancy_id)
    vacancy_to_delete.delete()

    return redirect('home')
def delete_summary(requset, summary_id):
    summary_to_delete = Summary.objects.get(id=summary_id)
    summary_to_delete.delete()

    return redirect('summary')


def summary_list(request):
    summaries = Summary.objects.all()
    return render(request, 'main/summary.html', {'title': 'Резюме', 'summaries': summaries})

def create_vacancy(request):#не пон
    error = ''
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'


    else:
        form = VacancyForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
def create_summary(request):#не пон
    error = ''
    if request.method == 'POST':
        form = SummaryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'


    else:
        form = SummaryForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_summary.html', context)

def filter_by_salary(request):
    form = FilterVacancy(request.POST)
    parameter = FilterVacancy
    filterd = Vacancy.objects.filter(salary__gte=parameter)
    context = {
        'title': f'Vacancies greater than {parameter}',
        'vacancies': filterd,
        'form': form
    }
    return render(request, 'main/index.html', filterd)

