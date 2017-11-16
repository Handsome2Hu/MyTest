#coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'&',views.index),
    url(r'^1',views.add2,name='add2'),
    url(r'^qrcode',views.generate_qrcode,name='qrcode'),
    url(r'^2',views.add3,name='add3'),
    url(r'^article/(?P<article_id>[0-9]+)$',views.article_page,name='article_page'),
    url(r'^edit/$',views.edit_page,name='edit_page'),
    url(r'^edit/action/$',views.edit_action,name='edit_action'),
]
