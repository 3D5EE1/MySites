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
from test_forms import views

urlpatterns = [
    path('test-forms', views.test_forms, name='test-forms'),
    path('search', views.search),
    path('file-input', views.file_input),
    # path('', views.form, name='form'),
    path('', views.ContactFormView.as_view(), name='form'),
    path('add-author/', views.add_author),
    path('add-article/', views.add_article),
    path('url-form', views.UrlView.as_view()),
]















