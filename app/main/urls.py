# from django.contrib import admin
from django.urls import path, include

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('main', views.index_main, name='index_main'),
    path('about/', views.about, name='about'),
    path('dm/', views.dm, name='dm'),
    path('cc_1/', views.cc_1, name='cc_1'),
    path('cc_2/', views.cc_2, name='cc_2'),

]