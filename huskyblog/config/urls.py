"""huskyblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from django.conf import settings

from blog.views import index, archive_list, essay_list, review_list, programming_list, post_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^archive/$', archive_list, name='archive_list'),
    url(r'^archive/essay/$', essay_list, name='essay_list'),
    url(r'^archive/review/$', review_list, name='review_list'),
    url(r'^archive/programming/$', programming_list, name='programming_list'),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^markdownx/', include('markdownx.urls')),
]

# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^.*(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#     ]
# urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
