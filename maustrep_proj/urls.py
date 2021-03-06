from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maustrep_proj.views.home', name='home'),
    # url(r'^maustrep_proj/', include('maustrep_proj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('maustrep.views',
    url(r'^$', 'main_trap'),
    url(r'^register/$', 'register_trap'),
    url(r'^list/$', 'list_trap_records'),
    url(r'^(?P<descriptor>\w+)/$', 'main_trap')
)
