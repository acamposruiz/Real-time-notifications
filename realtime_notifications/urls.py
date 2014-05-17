import notifications

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'realtime_notifications.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^inbox/notifications/', include(notifications.urls)),
    url(r'', include('user_sessions.urls', 'user_sessions'))
)
