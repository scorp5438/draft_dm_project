# from django.contrib import admin
from django.urls import path, include

from exam import views

app_name = 'exam'

urlpatterns = [
    path('', views.ExamView.as_view(), name='exam'),
    path('add/', views.AddInternView.as_view(), name='add_intern'),
    path('CheckList/', views.CheckListView.as_view(), name='CheckList'),
    path('edit/<int:pk>', views.ExamUpdateView.as_view(), name='edit_intern'),

]
