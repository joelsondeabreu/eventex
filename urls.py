from django.conf.urls.defaults import *
from core.views import*
from django.conf import settings

urlpatterns = patterns('',
	(r'^$', homepage),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$',
		'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT }),
	)