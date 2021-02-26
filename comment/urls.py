from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add_comment/(?P<pk>\d+)/$', views.add_comment,name='add_comment'),
    url(r'^comment_list/$', views.comment_list, name='comment_list'),
    url(r'^comment_del/(?P<pk>\d+)/$', views.comment_del, name='comment_del'),
    url(r'^confirmed/(?P<pk>\d+)/$', views.confirmed, name='confirmed'),
]