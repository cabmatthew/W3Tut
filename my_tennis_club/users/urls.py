from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
]

# http://127.0.0.1:8000/users/login_user