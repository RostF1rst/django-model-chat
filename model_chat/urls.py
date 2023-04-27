from django.urls import path

from model_chat import views

urlpatterns = [
    path('', views.chat, name='chat')
]
