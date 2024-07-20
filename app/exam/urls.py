# from django.contrib import admin
from django.urls import path, include

from exam import views

app_name = 'exam'

urlpatterns = [
    path('', views.exam_view, name='exam'),
    path('add/', views.add_intern, name='add_intern'),
    path('edit/', views.edit_intern, name='edit_intern'),

]
