from django.urls import path

from . import views

app_name = 'response-forum'

urlpatterns = [
    path('', views.ResponseListView.as_view(), name='list'),
    path('<int:pk>', views.ResponseDetailView.as_view(), name='details'),
    path('create', views.create_response, name='create'),
]
