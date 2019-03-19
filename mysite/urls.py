from django.contrib import admin
from django.urls import re_path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    re_path(r'^$', views.main, name='main'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^theme/', include(('theme.urls', 'theme'), namespace='theme')),
    re_path(r'^information/', include(('information.urls', 'information'), namespace='information')),
    re_path(r'^bulletinboard/', include(('bulletinboard.urls', 'buelletinboard'), namespace='bulletinboard')),
    re_path(r'^FAQ/', include(('FAQ.urls', 'FAQs'), namespace='FAQ'))
]


from django.conf import settings
from django.views import static


static_list = [
 (settings.STATIC_URL, settings.STATIC_ROOT),
 (settings.MEDIA_URL, settings.MEDIA_ROOT),
]
for (prefix_url, root) in static_list:
    if '://' not in prefix_url: # 외부 서버에서 서빙하는 것이 아니라면
        prefix_url = prefix_url.lstrip('/')
        url_pattern = r'^' + prefix_url + r'(?P<path>.+)'
        pattern = url(url_pattern, static.serve, kwargs={'document_root': root})
        urlpatterns.append(pattern)