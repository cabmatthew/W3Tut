from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('create/', views.create_view, name='memberform'),
    path('list/', views.memberlist_view, name='memberlist_view'),
    path('<int:id>/detail', views.memberdetail_view, name='memberdetail_view'),
    path('<int:id>/update', views.update_view, name='update_view'),
    path('<int:id>/delete', views.delete_view, name='delete_view'),
    path('<int:id>/ud', views.update_or_delete_view, name='update_or_delete_view'),
]