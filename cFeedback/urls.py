from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from cFeedback import settings
from customer_feedback import urls

#urlpatterns = patterns('django.views.static',
#                       (r'media/(?P<path>.*)','serve',
#                        {'document_root': settings.MEDIA_ROOT}), )
#urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cFeedback.views.home', name='home'),
    # url(r'^cFeedback/', include('cFeedback.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^customer feedback/', include(urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
