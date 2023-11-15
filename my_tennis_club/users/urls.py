from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('nologin', views.no_login, name='no_login'),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register_user"),
]

# http://127.0.0.1:8000/users/login_user