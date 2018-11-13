#!/usr/local/bin/python3.5
import unittest
import os
import sys
import requests
try:
    import urlparse
except:
    from urllib.parse import urlparse

class TestRedirect(unittest.TestCase):
    baseurl = ''
    desturl = ''
    def setUp(self):
        self.baseurl = os.environ["baseurl"]
        self.desturl = os.environ["desturl"]

    def checkRedirect(self, source, target, enforceHost=False):
        code = 0
        response = requests.get(source, allow_redirects=False)
        code = response.status_code
        location = source
        if 'Location' in response.headers:
            location = response.headers['Location']
    #		print(code, location)
        self.assertEqual(code, 302, 'Failed to get redirected to %s due to %s' % (source, code))
        locationPath = urlparse(location).path
        targetPath = urlparse(target).path
        self.assertEqual(locationPath, targetPath, 'Failed to redirect to the correct place. Expected %s but got %s' % (targetPath, locationPath))
        if enforceHost:
            sourceHost=urlparse(location).hostname
            targetHost=urlparse(target).hostname
            self.assertEqual(sourceHost, targetHost, 'Failed to redirect to the correct host. Expected %s but got %s' % (targetHost,sourceHost))
            sourceScheme = urlparse(location).scheme
            targetScheme = urlparse(target).scheme
            self.assertEqual(sourceScheme, targetScheme, 'Failed to redirect using the correct protocol.')


    def test_api(self):
        url = '%s/%s' % (self.baseurl, 'api')
        dest = '%s/%s' % ('https://iiif.io', 'api/index.html')
        self.checkRedirect(url, dest, True)

    def test_image(self):
        url = '%s/%s' % (self.baseurl, 'api/image/')
        dest = '%s/%s' % (self.desturl, 'api/image/2.1/')
        self.checkRedirect(url, dest)

    def test_presentation(self):
        url = '%s/%s' % (self.baseurl, 'api/presentation/index.html')
        dest = '%s/%s' % (self.desturl, 'api/presentation/2.1/')
        self.checkRedirect(url, dest)
    def test_validator(self):
        url = '%s/%s' % (self.baseurl, 'api/presentation/validator')
        dest = '%s/%s' % (self.desturl, 'api/presentation/validator/service')
        self.checkRedirect(url, dest)
    # why is this here?
    def test_ontology(self):
        url = '%s/%s' % (self.baseurl, 'api/presentation/2')
        dest = '%s/%s' % (self.desturl, 'api/presentation/2/ontology.xml')
        self.checkRedirect(url, dest)
    def test_metadata(self):
        url = '%s/%s' % (self.baseurl, 'api/metadata')
        dest = '%s/%s' % (self.desturl, 'api/presentation/2.1/')
        self.checkRedirect(url, dest)
    def test_presentation1(self):
        url = '%s/%s' % (self.baseurl, '/api/presentation/1.0')
        dest = '%s/%s' % (self.desturl, 'api/presentation/2.1/')
        self.checkRedirect(url, dest)
    def test_auth(self):
        url = '%s/%s' % (self.baseurl, '/api/auth/')
        dest = '%s/%s' % (self.desturl, 'api/auth/1.0/')
        self.checkRedirect(url, dest)
    def test_auth0(self):
        url = '%s/%s' % (self.baseurl, '/api/auth/0/')
        dest = '%s/%s' % (self.desturl, 'api/auth/1.0/')
        self.checkRedirect(url, dest)
    def test_search(self):
        url = '%s/%s' % (self.baseurl, '/api/search')
        dest = '%s/%s' % (self.desturl, 'api/search/1.0/')
        self.checkRedirect(url, dest)
    def test_api_redirect(self):
        url = '%s/%s' % (self.baseurl, 'api/image/')
        dest = '%s/%s' % ('https://iiif.io', 'api/image/2.1/')
        self.checkRedirect(url, dest, True)


if __name__ == '__main__':
    baseurl = 'http://localhost:5000'
    if len(sys.argv) == 2:
        baseurl = sys.argv[1]

    os.environ["baseurl"] = baseurl
    unittest.main()
