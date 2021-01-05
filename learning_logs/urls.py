""" Определяет схемы URL для learning_logs. """

from os import name
from django.urls import path
from learning_logs import views

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница тем
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по данной теме
    path('topics/<topic_id>', views.topic, name='topic')
]