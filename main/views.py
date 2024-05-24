# ТУТ МЫ БУДЕМ ПОКАЗЫВАТЬ КАКОЙ ЛИБО HTML ШАБЛОН ПРИ ПЕРЕХОДЕ НА НОВУЮ СТРАНИЦУ (ЕСЛИ ПОЛЬЗОВАТЕЛЬ ПЕРЕШЕЛ НА ГЛАУНЮ СТРАНИЦУ ТО МЫ ПОКАЖЕМ ЕМУ ТАКОЙ ТО ШАБЛОН)
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView
from .models import Vacancy, Summary
from .forms import SummaryForm, VacancyForm
def index(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'main/index.html', {'title': 'Вакансии', 'vacancies': vacancies})

def VacancyUpdate(UpdateView):
    model = Vacancy
    template_name = 'main/create.html'
    fields = ['title', 'salary', 'currency', 'description']

def summary_list(request):
    summaries = Summary.objects.all()
    return render(request, 'main/summary.html', {'title': 'Резюме', 'summaries': summaries})



def about(request):
    return render(request, 'main/about.html')

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

