from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from mainWebsite.views import PostDetail

from . import views

urlpatterns = [
    url(r'^$', views.UserDetail.as_view(), name='user-detail'),
    
    url(r'^blogs/$', views.UserPosts.as_view(), name='profile_blog'),
    url(r'^blogs/(?P<slug>.+)/$', views.UserPostDetail.as_view(), name='profile_blogs'),
    url(r'^portfolio/(?P<slug>.+)/$', views.UserPostDetail.as_view(), name='projects_detail'),
    url(r'^portfolio/$', views.UserPosts.as_view(), name='projects_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)