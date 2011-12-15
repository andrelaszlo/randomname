from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('names.views',
    # Examples:
    # url(r'^$', 'namesite.views.home', name='home'),
    # url(r'^namesite/', include('namesite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'main'),
    url(r'^male/?$', 'male'),
    url(r'^female/?$', 'female'),
    url(r'^comments/?$', 'comments'),
    url(r'^about/?$', 'about'),
    url(r'^share/(?P<name>.*)$', 'share'),
)
