from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^mylogin/$', views.mylogin, name='mylogin'),
    url(r'^logout/$', views.mylogout, name='mylogout'),
    url(r'^settings/$', views.site_settings, name='site_settings'),
    url(r'^aboutsettings/$', views.aboutsettings, name='aboutsettings'),
    url(r'^changepass/$', views.changepass, name='changepass'),
    url(r'^register/$', views.register, name='register'),
]