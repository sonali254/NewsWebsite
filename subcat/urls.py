from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^subcat_list/$', views.subcat_list, name='subcat_list'),
    url(r'^subcat_add/$', views.subcat_add, name='subcat_add'),

]