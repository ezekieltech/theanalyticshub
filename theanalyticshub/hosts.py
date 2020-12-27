from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns(
    '',
    host(r'',  settings.ROOT_URLCONF, name=' '),
    # host(r'(?P<username>\w+)',  'professionals.urls', name='user-area'),
    host(r'(ezekiel)',  'professionals.urls', name='user-area'),
)