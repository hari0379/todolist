from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('create_new/',views.create_new,name='create_new'),
    path('create_task/',views.create_task,name='create_task'),
]