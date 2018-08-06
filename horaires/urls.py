from django.urls import path
from . import views

app_name = 'horaires'
urlpatterns = [
    path('', views.index, name='index'),
]
