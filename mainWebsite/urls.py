from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='home'),
    url(r'^posts/(?P<slug>.+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^service/(?P<slug>.+)/$', views.ServiceDetail.as_view(), name='service_detail'),
    url(r'^services/$', views.ServiceList.as_view(), name='services'),
    # url(r'^department/(?P<user>.+)/$', views.ProfileDetail.as_view(), name='profile_detail'),
    # url(r'^profile/$', views.ProfileList.as_view(), name='profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)