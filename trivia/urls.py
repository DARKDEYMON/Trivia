from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from trivia.aplicaciones.sistema.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trivia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', usuario_login),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)