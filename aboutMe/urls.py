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
from aboutMe import views

urlpatterns = [
    path('', views.aboutMe, name='aboutMe'),
    path('aboutMe/_main', views.main, name='main'),
    path('aboutMe/', views.test),
    path('aboutMe/page<int:num>', views.test),
    path('aboutMe/test-request', views.test_request),
    path('aboutMe/form-handler', views.form),
    path('aboutMe/template', views.template)
]

