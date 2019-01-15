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
from django.conf.urls import url
from account import views

urlpatterns = [
    path('creation/', views.creation, name='creation'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate,
        name='activate'),

    path('confirm', views.confirm)  # for confirm
]


# from django.urls import path
# from account import views
#
# urlpatterns = [
#     path('home/', views.home, name='home'),
#     path('creation/', views.CreationView.as_view(), name='creation')
#     # path('', views.profile, name="login"),  # первый способ
#     # path('login/', auth_views.LoginView.as_view(template_name='test_account/login1.html'), name='login'),
# второй способ
#     # path('', views.home, name='home'),
#     # path('auth-app/login/', auth_views.LoginView.as_view(template_name='test_account/login1.html'), name='login'),
#     # path('auth-app/logout/', auth_views.LogoutView.as_view(next_page='/test_account/'), name='logout'),
#     # path('auth-app/', views.auth_app_home, name='auth-app-home'),
#     # path('auth-app/sign-up', views.auth_app_sign_up, name='auth-app-sign-up'),
#     # path('creation/', views.CreationView.as_view(), name='creation'),
# ]



