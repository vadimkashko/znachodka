from django.conf import settings
from django.urls import path

from . import views

if settings.DEBUG:
    urlpatterns = [
        path('', views.index, name='index'),
        path('<int:item_id>/', views.item, name='item')
    ]
