from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'track_activity.views.list_activity',name='list'),
    url(r'^add_activity/$', 'track_activity.views.save_activity',name='new_activity'),
    url(r'^activity_detail/(\d+)/$', 'track_activity.views.activity_detail',name='activity_detail'),

)
