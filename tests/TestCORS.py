#!/usr/bin/env python3
import unittest
import os
import requests

class TestCORS(unittest.TestCase):
    baseurl = ''
    def setUp(self):
        self.baseurl = os.environ["baseurl"]

    def test_xml_cors(self):
        url = "%s/%s" % (self.baseurl, 'api/cookbook/recipe/0068-newspaper/newspaper_issue_1-alto_p1.xml')

        response = requests.get(url, allow_redirects=False)
        code = response.status_code
        self.assertEqual(code,200, 'Failed to get required xml file for CORS testing. Got response %s from URL %s' % (code, url))

        # Check CORS headers
        self.assertTrue('Access-Control-Allow-Origin' in response.headers, 'Missing Access-Control-Allow-Origin header from %s' % url)
        self.assertEqual(response.headers['Access-Control-Allow-Origin'],"*", 'Expected header Access-Control-Allow-Origin:* but was Access-Control-Allow-Origin:%s' % (response.headers['Access-Control-Allow-Origin']))

if __name__ == '__main__':
    os.environ["baseurl"] = 'http://localhost:9001'
    unittest.main()
