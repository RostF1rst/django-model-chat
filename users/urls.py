from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register', views.UserRegistrationView.as_view(), name='register'),
    path('settings/', views.settings, name='settings'),
    path('<int:pk>/', views.user_page, name='user_page'),
    path('me', views.user_page_me, name='user_page_me'),
    path('fake', views.create_fake_user),
]
