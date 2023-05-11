from django.urls import path

from . import views, ajax

app_name = 'response-forum'

urlpatterns = [
    # views
    path('', views.ResponseListView.as_view(), name='list'),
    path('<int:pk>', views.ResponseDetailView.as_view(), name='details'),
    path('create', views.create_response, name='create'),

    # ajax
    path('get_list', ajax.get_list_of_responses, name='list_of_responses'),

    # test
    path('fake', views.create_fake_posts),
]
