from django.conf.urls.defaults import *

from django.conf import settings 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from shopjet.my_db.views import *
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^shopjet/', include('shopjet.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'my_db.views.show'),
    (r'^admin/', include(admin.site.urls)),
    (r'^products/$','my_db.views.show_product'),
    (r'^table/$','my_db.views.table'),
    (r'^generate_tracking/', 'my_db.views.generate_tracking' ),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^tag_test/','my_db.views.tag_test' ),
    (r'^crawler/', include('crawler.urls')),
)
