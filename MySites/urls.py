"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('mysites-admin/', admin.site.urls),
    path('', include('aboutMe.urls')),
    path('account/login/', auth_views.LoginView.as_view(template_name='account/login.html')),
    path('art3d', include('art3d.urls')),
    path('cinema', include('cinema.urls')),
    path('comingSoon', include('comingSoon.urls')),
    path('company', include('company.urls')),
    path('detective', include('detective.urls')),
    path('games', include('games.urls')),
    path('menu', include('menu.urls')),
    path('planets', include('planets.urls')),
    path('shop', include('shop.urls')),
    path('stickers', include('stickers.urls')),
    path('tattoo', include('tattoo.urls')),
    path('test_forms/', include('test_forms.urls')),
    path('test_models', include('test_models.urls')),
    path('test_templates/', include('test_templates.urls')),
]

