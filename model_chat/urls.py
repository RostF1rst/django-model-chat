from django.urls import path

from . import views, ajax

app_name = 'model-chat'

urlpatterns = [
    # views
    path('', views.chat, name='chat'),

    # ajax paths
    path('get_response/', ajax.get_response, name='get-response')
]
