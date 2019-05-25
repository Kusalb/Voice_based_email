from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('speech', views.voicetotext, name='speech'),
    path('compose', views.compose, name= 'compose')
]