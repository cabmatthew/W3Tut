from django.urls import path
from . import views
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('testing/', views.testing, name='testing'),
    path('create/', views.create_view, name='memberform'),
    path('list/', views.memberlist_view, name='memberlist_view'),
    path('<int:id>/detail', views.memberdetail_view, name='memberdetail_view'),
    path('<int:id>/ud', views.update_or_delete_view, name='update_or_delete_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
