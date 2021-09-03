from django.urls import path

from . import views


urlpatterns = [
    path('auth/login', views.AuthLogin.as_view(), name='login-auth'),
    # path('auth/login', views.AuthLogin().as_view(), name='register-auth'),
]