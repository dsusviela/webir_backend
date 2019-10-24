from django.urls import path

from . import views

urlpatterns = [
    path('show', views.list_postgraduates, name='show'),
    path('', views.index, name='index'),
]