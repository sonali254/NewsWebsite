from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^contactapp/$', views.contact_add, name='contact_add'),
    url(r'^contactform/$', views.contact_show, name='contact_show'),
    url(r'^panel/contactform/del/(?P<pk>\d+)/$', views.contact_del, name='contact_del'),

]
