from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.LoginForm.as_view())
]