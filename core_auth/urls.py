from django.urls import path

from . import views


urlpatterns = [
    path('echo/', views.TestView.as_view(), name='echo-view'),
]