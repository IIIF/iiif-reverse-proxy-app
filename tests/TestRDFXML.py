#!/usr/local/bin/python3.5
import unittest
import os
import sys
import requests

class TestRDFXML(unittest.TestCase):
    baseurl = ''
    def setUp(self):
        self.baseurl = os.environ["baseurl"]

    def checkRedirect(self, source, target, host):
        url = '%s/%s' % (self.baseurl, 'api/presentation/2/ontology.xml')
        response=urlopen(url)
        header=response.info().get('Content-Type')
        self.assertEqual(header, 'application/rdf+xml', 'ontology.xml returned Content-Type %s not application/rdf+xml.' % header)

if __name__ == '__main__':
    baseurl = 'http://localhost:5000'
    if len(sys.argv) == 2:
        baseurl = sys.argv[1]

    os.environ["baseurl"] = baseurl

    unittest.main()
