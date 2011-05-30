from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings
from django.contrib import admin
from autoregister import autoregister

admin.autodiscover()
autoregister('pixelcode')

handler500 # Pyflakes

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^admin_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT}),
    url(r'^$', 'pixelcode.views.index', name="index"),
    (r'^blog/', include('pixelcode.blog.urls')),
    url(r'^contact-form/$', 'pixelcode.views.contact_form', name='contact_form'),
    url(r'^(?P<nav>[-\w]+)/$', 'pixelcode.views.nav', name='nav'),
    url(r'^(?P<nav>[-\w]+)/(?P<subnav>[-\w]+)/$', 'pixelcode.views.subnav', name='subnav'),
    url(r'^(?P<nav>[-\w]+)/(?P<subnav>[-\w]+)/(?P<subsubnav>[-\w]+)/$', 'pixelcode.views.subsubnav', name='subsubnav'),
)
