from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.booking, name='booking'),
    re_path(r'^all/$', views.booking_list, name='booking_list'),
]
