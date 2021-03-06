"""FileShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from Users import views as user_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('MainApp.urls')),
    url(r'^login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    url(r'^register/', user_views.register, name='register'),
    url(r'^profile/', user_views.profile, name='profile'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
]
