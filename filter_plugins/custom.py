# Thanks to https://gist.github.com/halberom/a5aebb34da179fdce91a1bd018ec2805
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from urlparse import urlparse

def parse_url(url):
    """return a dict, of the parsed elements"""
    result = {}

    o = urlparse(url)

    result['scheme'] = o.scheme
    result['port'] = o.port
    result['url'] = o.geturl()
    result['path'] = o.path
    result['netloc'] = o.netloc
    result['query'] = o.query
    result['hostname'] = o.hostname

    # set scheme port if no port
    if o.port is not None:
        result['scheme_port'] = o.port
    elif o.scheme == "https":
        result['scheme_port'] = 443
    else:
        result['scheme_port'] = 80
    return result

class FilterModule(object):

    def filters(self):
        return {
            "parse_url": parse_url
        }
