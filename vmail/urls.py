from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('speech', views.voicetotext, name='speech'),
    path('compose', views.compose, name= 'compose'),
    path('compose_message', views.compose_message, name='compose_message'),
    path('compose_subject', views.compose_subject, name='compose_subject'),
    path('compose_recipent', views.compose_recipent, name='compose_recipent'),
    path('compose_sent', views.compose_send, name='compose_send'),
    path('inbox', views.inbox, name='inbox')
]


