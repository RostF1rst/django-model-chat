from django.urls import path

from model_chat import views

app_name = 'model-chat'

urlpatterns = [
    path('', views.chat, name='chat')
]
