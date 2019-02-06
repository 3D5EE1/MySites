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
from django.urls import path
from about_me import views
from account import views as account_views
from message import views as message_views

urlpatterns = [
    path('', views.about_me, name='about_me'),
    path('profile', account_views.profile, name='profile'),
    path('login/<str:site_redirect>', account_views.login_redirect, name='login'),
    path('legal', views.legal, name='legal'),
    path('license-agreement/<str:site>', views.license_agreement, name='license_agreement'),
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),
    path('careers', views.careers, name='careers'),
    path('about', views.about, name='about'),
    path('support', views.support, name='support'),
    path('contact', views.contact, name='contact'),
    path('press', views.press, name='press'),
    path('api', views.api, name='api'),
    path('career-administrator', views.career_administrator, name='career_administrator'),
    path('coming-soon', views.coming_soon, name='coming_soon'),
    path('message/', message_views.message),
]

