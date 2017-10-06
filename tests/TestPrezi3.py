#!/usr/local/bin/python3
import unittest
import os
import sys
import requests

class TestPrezi3(unittest.TestCase):
    baseurl = ''
    desturl = ''
    def setUp(self):
        self.baseurl = os.environ["baseurl"].replace('localhost','0.0.0.0')
        self.desturl = os.environ["desturl"].replace('localhost','0.0.0.0')

    def checkOK(self, source, host):
        code = 0
        response = requests.get(source, allow_redirects=False, headers={'host': host})
        code = response.status_code
        self.assertEqual(code, 200, 'Failed to get 200 from host %s due to %s' % (host, code))

    def redirectCheck(self, url, target):
        code = 0
        response = requests.get(url, allow_redirects=False, headers={'host': 'prezi3.iiif.io'})
        code = response.status_code
        location = url
        if 'Location' in response.headers:
            location = response.headers['Location']
        self.assertEqual(code, 302, 'Failed to get redirected to %s due to %s' % (url, code))
        self.assertEqual(location, target, 'Failed to redirect to the correct place. Expected %s but got %s' % (target, location))

    def test_prezi3(self):
        url = '%s/%s' % (self.baseurl, 'api/presentation/3.0/')
        self.checkOK(url, 'prezi3.iiif.io')

    def test_apiredirect(self):
        url = '%s/%s' % (self.baseurl, '')
        target = 'http://prezi3.iiif.io/api/index.html'
        self.redirectCheck(url, target)

    def test_presentationMissingslash(self):
        url = '%s/%s' % (self.baseurl, 'api/presentation/3.0')
        target = 'http://prezi3.iiif.io/api/presentation/3.0/'
        self.redirectCheck(url, target)

if __name__ == '__main__':
    baseurl = 'http://localhost:5000'
    if len(sys.argv) == 2:
        baseurl = sys.argv[1]

    os.environ["baseurl"] = baseurl
    os.environ["desturl"] = baseurl


    unittest.main()
