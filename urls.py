from django.conf.urls.defaults import *
from videogallery.views import *
import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
# test
#urlpatterns = patterns('',
    # Example:
    # (r'^video_gallery/', include('video_gallery.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
#)

site_media = os.path.join(os.path.dirname(__file__), 'site_media')
videos = os.path.join(os.path.dirname(__file__), 'videos')

urlpatterns = patterns('',
(r'^$', main_page),
(r'^user/(\w+)/$', user_page),
(r'^users/$', users_page),
(r'^login/$', 'django.contrib.auth.views.login'),
(r'^logout/$', logout_page),
(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media}),
(r'^videos/(?P<path>.*)$', 'django.views.static.serve', {'document_root': videos}),
(r'^register/$', register_page),
(r'^register/success/$', register_success),
(r'^upload/$', video_upload_page),
)

