from django.urls import path
from . import views

app_name = 'autre'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('ajouter_article', views.ajouter_article, name='ajouter_article'),
]
