from django.conf.urls import url

urlpatterns = [ url(r'^user/(?P<username>[-\w]+)/$',
                    'marcapp.views.bookmark_user',
                    name='marcapp_bookmark_user'),
                url(r'^$', 'marcapp.views.bookmark_list',
                    name='marcapp_bookmark_list'),]