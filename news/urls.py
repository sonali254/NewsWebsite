from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^news/(?P<word>.*)/$', views.news_details, name='news_details'),
    url(r'^newslist$', views.newslist, name='newslist'),
    url(r'^newsadd$', views.newsadd, name='newsadd'),
    url(r'^news_delete/(?P<pk>\d+)/$', views.news_delete, name='news_delete'),
    url(r'^news_edit/(?P<pk>\d+)/$', views.news_edit, name='news_edit'),
    url(r'^news_publish/(?P<pk>\d+)/$', views.news_publish, name='news_publish'),
    url(r'^all/news/(?P<word>.*)/$', views.news_all_show, name='news_all_show'),

]