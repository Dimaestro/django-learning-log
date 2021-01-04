""" Определяет схемы URL для learning_logs. """

from django.urls import path
from learning_logs import views

urlpatterns = [
    # Домашняя страница
    path('', views.index)
]