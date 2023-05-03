from django.urls import path

from . import views, ajax

app_name = 'model-chat'

urlpatterns = [
    path('', views.chat, name='chat'),
    path('get_response/', ajax.get_response, name='get-response')
]
