from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^cat_list/$', views.cat_list, name='cat_list'),
    url(r'^cat_add/$', views.cat_add, name='cat_add'),

]