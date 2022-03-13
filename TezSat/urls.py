from django.contrib import admin
from django.urls import path, include
from LocalUser.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('home', home),
]
