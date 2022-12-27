from django.urls import path
from . import views


app_name = "app1"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('data_list/', views.DataListView.as_view(), name='data_list'),
]
