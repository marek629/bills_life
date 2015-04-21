from django.conf.urls import patterns, include, url
from django.contrib import admin

from events import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bills_life.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/(\w*)', views.index)
)
