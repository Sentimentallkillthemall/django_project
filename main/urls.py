from django.urls import path
# from .views import VacancyUpdate
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create_vacancy, name='create'),
    path('summary', views.summary_list, name='summary'),
    path('update/<int:vacancy_id>/', views.update_vacancy, name='update-vacancy'),
    path('delete/<int:vacancy_id>/', views.delete_vacancy, name='delete-vacancy')

]
