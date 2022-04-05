
from django.conf.urls import include
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib import admin
from organizer import urls as organizer_urls

from .views import category_detail, ShowCategories

urlpatterns = [

    url(r'^$', ShowCategories.as_view(), name='organizer_categories'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^(?P<slug>[\w\-]+)/$', category_detail, name='organizer_category_detail'),
	url(r'^admin/', include(admin.site.urls)),
	]
