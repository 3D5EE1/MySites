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


urlpatterns = [
    path('my-sites-admin/', admin.site.urls, name='my-sites-admin'),
    path('', include('app_about_site.urls')),
    # первый способ path('accounts/', include('django.contrib.auth.urls')),
    # первый способ path('accounts/profile/', include('app_account.urls')),
    path('account/', include('app_account.urls')),
    path('art3d', include('app_art3d.urls')),
    path('cinema', include('app_cinema.urls')),
    path('message/', include('app_message.urls')),
    path('company/', include('app_company.urls')),
    path('detective', include('app_detective.urls')),
    path('games', include('app_games.urls')),
    path('menu', include('app_menu.urls')),
    path('planets', include('app_planets.urls')),
    path('shop', include('app_shop.urls')),
    path('stickers', include('app_stickers.urls')),
    path('tattoo', include('app_tattoo.urls')),
    path('test-forms/', include('app_test_forms.urls')),
    path('test-models.py', include('app_test_models.urls')),
    path('test-templates/', include('app_test_templates.urls')),
]

