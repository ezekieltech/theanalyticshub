from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns(
    '',
    host(r'', 'theanalyticshub.urls', name=' '),
    host(r'(?P<username>\w+)\.127\.0.0.1\:8000',  'mainWebsite.urls', name='user-area'),
)