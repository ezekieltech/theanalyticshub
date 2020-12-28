from django_hosts.resolvers import reverse_host


# subdomain is usually of the format subdomain.domain.com
# Logically, subdomain is tied to the users
# this function returns the subdomain which can be used in the view for instance
def getUsernameFromSubdomain():
    host = reverse_host('user-area', args=('ezekiel',))
    host = host.split('.')[0]
    return host