from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page that takes user input
]
