from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^newsletter_add/$', views.newsletter_add, name='newsletter_add'),
    url(r'^email/$', views.email, name='email'),
    url(r'^phone/$', views.phone, name='phone'),
    url(r'^news_txt_del/(?P<pk>\d+)/(?P<num>\d+)/$', views.news_txt_del, name='news_txt_del'),
]