from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='accounts'
urlpatterns = [
    path('login/', auth_views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]
