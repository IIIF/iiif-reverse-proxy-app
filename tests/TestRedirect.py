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

    def checkRedirect(self, source, target, enforceHost=False, target_code=302):
        code = 0
        response = requests.get(source, allow_redirects=False)
        code = response.status_code
        location = source
        if 'Location' in response.headers:
            location = response.headers['Location']
    #		print(code, location)
        self.assertEqual(code, target_code, 'Failed to get correct code redirected to %s from %s, recieved code: %s' % (target, source, code))
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
        dest = '%s/%s' % (self.desturl, 'api/image/3.0/')
        self.checkRedirect(url, dest)

    def test_presentation(self):
        url = '%s/%s' % (self.baseurl, 'api/presentation/index.html')
        dest = '%s/%s' % (self.desturl, 'api/presentation/3.0/')
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
        dest = '%s/%s' % (self.desturl, 'api/auth/2.0/')
        self.checkRedirect(url, dest)
    def test_auth0(self):
        url = '%s/%s' % (self.baseurl, '/api/auth/0/')
        dest = '%s/%s' % (self.desturl, 'api/auth/1.0/')
        self.checkRedirect(url, dest)
    def test_search(self):
        url = '%s/%s' % (self.baseurl, '/api/search')
        dest = '%s/%s' % (self.desturl, 'api/search/2.0/')
        self.checkRedirect(url, dest)
    def test_api_redirect(self):
        url = '%s/%s' % (self.baseurl, 'api/image/')
        dest = '%s/%s' % ('https://iiif.io', 'api/image/3.0/')
        self.checkRedirect(url, dest, True)

    def test_editor_policy(self):
        url = '%s/%s' % (self.baseurl, 'api/annex/notes/editors/')
        dest = '%s/%s' % (self.desturl, 'community/policy/editorial/')
        self.checkRedirect(url, dest)

    def test_editor_policy_index(self):
        url = '%s/%s' % (self.baseurl, 'api/annex/notes/editors/index.html')
        dest = '%s/%s' % (self.desturl, 'community/policy/editorial/')
        self.checkRedirect(url, dest)

   # def test_slash404(self):
   #     url = '%s/%s' % (self.baseurl, '/404.html')
   #     dest = '%s/%s' % ('https://iiif.io', '/404.html')
   #     self.checkRedirect(url, dest, True)

    def test_404(self):
        url = '%s/%s' % (self.baseurl, '/estste.html')
        dest = '%s/%s' % ('https://iiif.io', '/404.html')
        self.checkRedirect(url, dest, True, target_code=301)

    def test_nested404(self):
        url = '%s/%s' % (self.baseurl, '/estste/setestse')
        dest = '%s/%s' % ('https://iiif.io', '/404.html')
        self.checkRedirect(url, dest, True, target_code=301)

    # 2021 Website move shared-canvas now in the api directory
    def test_sharedCanvas(self):    
        url = '%s/%s' % (self.baseurl, 'model/shared-canvas/1.0/')
        dest = '%s/%s' % ('https://iiif.io', 'api/model/shared-canvas/1.0/')
        self.checkRedirect(url, dest, True, target_code=301)

    # 2021 Website IIIF logo moved
    def test_iiiflogo(self):
        url = '%s/%s' % (self.baseurl, 'img/logo-iiif-34x30.png')
        dest = '%s/%s' % ('https://iiif.io', 'assets/uploads/logos/logo-iiif-34x30.png')
        self.checkRedirect(url, dest, True, target_code=302)


if __name__ == '__main__':
    baseurl = 'http://localhost:5000'
    if len(sys.argv) == 2:
        baseurl = sys.argv[1]

    os.environ["baseurl"] = baseurl
    unittest.main()
