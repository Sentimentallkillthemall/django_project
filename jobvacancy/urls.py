from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('main.urls')),
    path('', include('user.urls')),
    path('summary/',include('main.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout', LogoutView.as_view(), name='logout')

]
