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
from account import views as account_views

urlpatterns = [
    path('my-sites-admin/', admin.site.urls, name='my-sites-admin'),
    path('', include('about_me.urls')),
    # первый способ path('accounts/', include('django.contrib.auth.urls')),
    # первый способ path('accounts/profile/', include('account.urls')),
    path('account/', include('account.urls')),
    path('profile', account_views.profile, name='profile'),
    path('privacy-policy', account_views.privacy_policy, name='privacy_policy'),
    path('legal', account_views.legal, name='legal'),
    path('login/<str:site_redirect>', account_views.login_redirect, name='login'),
    path('art3d', include('art3d.urls')),
    path('cinema', include('cinema.urls')),
    path('coming-soon/', include('coming_soon.urls')),
    path('company', include('company.urls')),
    path('detective', include('detective.urls')),
    path('games', include('games.urls')),
    path('menu', include('menu.urls')),
    path('planets', include('planets.urls')),
    path('shop', include('shop.urls')),
    path('stickers', include('stickers.urls')),
    path('tattoo', include('tattoo.urls')),
    path('test-forms/', include('test_forms.urls')),
    path('test-models.py', include('test_models.urls')),
    path('test-templates/', include('test_templates.urls')),
]

