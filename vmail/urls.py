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
    path('compose_sent1', views.compose_send1, name='compose_send1'),
    path('inbox', views.inbox, name='inbox'),
    path('compose_send', views.compose_send, name='compose_send'),
    path('discard', views.compose_discard, name='compose_discard'),
    path('outbox', views.outbox, name='outbox'),
    path('draft', views.draft, name='draft')

]


