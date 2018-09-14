#!/usr/local/bin/python3.6
import unittest
import os
import requests

class TestHttps(unittest.TestCase):
    baseurl = ''
    def setUp(self):
        self.baseurl = os.environ["baseurl"]

    def test_redirect(self):
        url = "%s/%s" % (self.baseurl, 'index.html')

        headers = {'X-Forwarded-Proto': 'http'}
        response = requests.get(url, headers=headers, allow_redirects=False)
        code = response.status_code
        self.assertEqual(code,301, 'Failed to redirect from http to https got code %s from URL %s' % (code, url))

        location=response.headers['Location']
        self.assertEqual(location,"https://iiif.io/index.html", 'Failed to redirect to correct place. Expected to go to https://iiif.io but was forwarded to %s' % (location))

        # Check CORS headers
        self.assertTrue('Access-Control-Allow-Origin' in response.headers, 'Missing Access-Control-Allow-Origin header from %s' % location)
        self.assertEqual(response.headers['Access-Control-Allow-Origin'],"*", 'Expected header Access-Control-Allow-Origin:* but was Access-Control-Allow-Origin:%s' % (response.headers['Access-Control-Allow-Origin']))

    def test_noredirect(self):
        url = self.baseurl
        headers = {'X-Forwarded-Proto': 'https'}
        response = requests.get(url, headers=headers, allow_redirects=False)

        code = response.status_code
        self.assertEqual(code,200, 'Failed expected 200 but got code %s for https page: %s' % (code, url))

if __name__ == '__main__':
    os.environ["baseurl"] = 'http://localhost:9001'
    unittest.main()
