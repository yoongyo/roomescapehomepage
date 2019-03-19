from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.board_list, name='board_list'),
    re_path(r'^new/$', views.board_new, name='board_new'),
    re_path(r'^(?P<pk>[\d]+)/$', views.board_detail, name='board_detail'),
]
