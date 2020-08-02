from django.contrib import admin
from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('video/<int:pk>', views.video, name='video'),
    path('video', views.all_video, name='allvideo'),
    path('khawatir/<int:pk>', views.khawatir, name='khawatir'),
    path('khawatir/', views.all_khawatir, name='allkhawatir'),
    path('sound/<int:pk>', views.sound, name='sound'),
    path('sound/', views.all_sound, name='allsound'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),

]
