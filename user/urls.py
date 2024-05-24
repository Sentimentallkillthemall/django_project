from django.urls import path
from user import views


urlpatterns = [
    path('signup/', views.Sign.as_view(), name='signup')
]