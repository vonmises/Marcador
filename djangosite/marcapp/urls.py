from django.conf.urls import url

urlpatterns = [ url(r'^user/(?P<username>[-\w]+)/$',
                    'marcapp.views.bookmark_user',
                    name='marcapp_bookmark_user'),
                url(r'^create/$', 'marcapp.views.bookmark_create',
                    name='marcapp_bookmark_create'),
                url(r'^edit/(?P<pk>\d+)/$', 'marcapp.views.bookmark_edit',
                    name='marcapp_bookmark_edit'),
                url(r'^$', 'marcapp.views.bookmark_list',
                    name='marcapp_bookmark_list'),]