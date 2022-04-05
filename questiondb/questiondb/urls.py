
from datetime import datetime
from django.conf.urls import include, url
from django.contrib import admin
import django.contrib.auth.views

from django.conf.urls import include, url
from django.contrib import admin
from organizer import urls as organizer_urls
from .views import redirect_root


urlpatterns = [

    url(r'^$', redirect_root),
    #url(r'^contact$', app.views.contact, name='contact'),
    url(r'^admin/', include(admin.site.urls), name='admin' ),
	url(r'^zzonawav/', include(organizer_urls)),

]
