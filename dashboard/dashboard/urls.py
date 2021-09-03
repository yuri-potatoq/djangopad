from django.urls import path

from . import views


urlpatterns = [
    path("entry/", views.EntryDash.as_view(), name="entry"),
    path('login/', views.LoginForm.as_view(), name='login'),
    path('register/', views.RegisterForm.as_view(), name='register'),
]