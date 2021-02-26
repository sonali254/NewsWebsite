from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^trending_add/$', views.trending_add, name='trending_add'),
    url(r'^trending_edit/(?P<pk>\d+)$', views.trending_edit, name='trending_edit'),
    url(r'^trending_delete/(?P<pk>\d+)/$', views.trending_delete, name='trending_delete'),


]