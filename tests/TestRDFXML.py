#!/usr/local/bin/python3.5
import unittest
import os
import sys
import requests
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
from urllib import request


class TestRDFXML(unittest.TestCase):
    baseurl = ''
    def setUp(self):
        self.baseurl = os.environ["baseurl"]

    def checkRedirect(self, source, target, host):
        url = '%s/%s' % (self.baseurl, 'api/presentation/2/ontology.xml')
        response=urlopen(url)
        header=response.info().get('Content-Type')
        self.assertEqual(header, 'application/rdf+xml', 'ontology.xml returned Content-Type %s not application/rdf+xml.' % header)

    def test_jsonldmimetype(self):
        url = '%s/%s' % (self.baseurl, 'api/image/2#')
        opener = request.build_opener()
        opener.addheaders = [('Accept', 'application/rdf+xml')]
        response=opener.open(url)
        location=response.geturl()
        self.assertEqual(location, 'https://iiif.io/api/image/2/ontology.xml', 'Failed to redirect with accept')

        response=urlopen(url)
        self.assertEqual(response.geturl(), 'https://iiif.io/api/image/2.1/', 'Failed to correctly redirect without accept')

if __name__ == '__main__':
    baseurl = 'http://localhost:5000'
    if len(sys.argv) == 2:
        baseurl = sys.argv[1]

    os.environ["baseurl"] = baseurl

    unittest.main()
