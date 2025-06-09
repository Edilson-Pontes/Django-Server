from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.api_root, name='root'),
    path('users/', views.user_list, name='user_list'),
    path('data/', views.data_list, name='data_list'),
]