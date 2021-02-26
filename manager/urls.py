from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^managerlist/$', views.managerlist, name='managerlist'),
    url(r'^manager_del/(?P<pk>\d+)/$', views.manager_del , name='manager_del'),
    url(r'^manager_group/$', views.manager_group, name='manager_group'),
    url(r'^manager_perms/$', views.manager_perms, name='manager_perms'),
    url(r'^manager_group_add/$', views.manager_group_add, name='manager_group_add'),
    url(r'^manager_group_del/(?P<name>.*)/$', views.manager_group_del , name='manager_group_del'),
    url(r'^users_group/(?P<pk>\d+)/$', views.users_group, name='users_group'),
    url(r'^add_users_to_group/(?P<pk>\d+)/$', views.add_users_to_group, name='add_users_to_group'),
    url(r'^del_users_to_group/(?P<pk>\d+)/(?P<name>.*)/$', views.del_users_to_group, name='del_users_to_group'),
    url(r'^manager_perms_del/(?P<name>.*)/$', views.manager_perms_del , name='manager_perms_del'),
    url(r'^manager_perms_add/$', views.manager_perms_add, name='manager_perms_add'),
    url(r'^users_perms/(?P<pk>\d+)/$', views.users_perms, name='users_perms'),
    url(r'^users_perms_add/(?P<pk>\d+)/$', views.users_perms_add, name='users_perms_add'),
    url(r'^users_perms_del/(?P<pk>\d+)/(?P<name>.*)/$', views.users_perms_del , name='users_perms_del'),
    url(r'^groups_perms/(?P<name>.*)/$', views.groups_perms, name='groups_perms'),
    url(r'^groups_perms_del/(?P<gname>.*)/(?P<name>.*)/$', views.groups_perms_del, name='groups_perms_del'),
    url(r'^groups_perms_add/(?P<name>.*)/$', views.groups_perms_add, name='groups_perms_add'),
]
