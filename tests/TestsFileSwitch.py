#!/usr/local/bin/python3.5
import unittest
import os
from urllib.request import urlopen
from urllib import request
import requests

class TestFileSwitch(unittest.TestCase):
    baseurl = ''
    def setUp(self):
        self.baseurl = os.environ["baseurl"]

    def test_webp(self):
        url = '%s/%s' % (self.baseurl, 'assets/images/heroes/event_2.webp')
        code = 0
        try:
            response = requests.get(url, allow_redirects=False)
            code = response.status_code
        except request.HTTPError as error:	
            code = error.code

        self.assertEqual(code, 200, 'Missing test webp %s from %s' % (code, url))

        self.assertEqual(response.headers['content-type'], 'image/png', "Expected png as I didn't specify supports webp")

        try:
            response = requests.get(url, headers={ "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" }, allow_redirects=False)
            code = response.status_code
        except request.HTTPError as error:	
            code = error.code

        self.assertEqual(response.headers['content-type'], 'image/webp', "Expected webp as I can handle a webp")

if __name__ == '__main__':
    baseurl = 'http://localhost:9001'
    os.environ["baseurl"] = baseurl
    unittest.main()
