#!/usr/bin/env python3
import unittest
import os
import requests

class TestCORS(unittest.TestCase):
    baseurl = ''
    def setUp(self):
        self.baseurl = os.environ["baseurl"]

    def test_options_cors(self):
        url = "%s/%s" % (self.baseurl,'api/cookbook/recipe/0068-newspaper/newspaper_issue_1-manifest.json')    
        headers = {
            "Origin": "https://example.com",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "User-Agent": "HTTPie/3.2.1"
        }

        response = requests.options(url, allow_redirects=False, headers=headers)
        code = response.status_code
        self.assertEqual(code,204, 'Failed to get newspaper json file for CORS testing. Got response %s from URL %s\n%s' % (code, url, response.text))

        # Check CORS headers
        self.assertTrue('Access-Control-Allow-Origin' in response.headers, 'Missing Access-Control-Allow-Origin header from %s' % url)
        self.assertEqual(response.headers['Access-Control-Allow-Origin'],"*", 'Expected header Access-Control-Allow-Origin:* but was Access-Control-Allow-Origin:%s' % (response.headers['Access-Control-Allow-Origin']))

    def test_xml_cors(self):
        url = "%s/%s" % (self.baseurl, 'api/cookbook/recipe/0068-newspaper/newspaper_issue_1-alto_p1.xml')

        response = requests.get(url, allow_redirects=False)
        code = response.status_code
        self.assertEqual(code,200, 'Failed to get required xml file for CORS testing. Got response %s from URL %s' % (code, url))

        # Check CORS headers
        self.assertTrue('Access-Control-Allow-Origin' in response.headers, 'Missing Access-Control-Allow-Origin header from %s' % url)
        self.assertEqual(response.headers['Access-Control-Allow-Origin'],"*", 'Expected header Access-Control-Allow-Origin:* but was Access-Control-Allow-Origin:%s' % (response.headers['Access-Control-Allow-Origin']))

        self.assertEqual(response.headers['Content-Type'],"text/xml", 'Expected header Content-Type: text/xml but was Content-Type: %s' % (response.headers['Content-Type']))

    def test_vtt_cors(self):
        url = "%s/%s" % (self.baseurl, 'api/cookbook/recipe/0074-multiple-language-captions/Per_voi_signore_Modelli_francesi_en.vtt')

        response = requests.get(url, allow_redirects=False)
        code = response.status_code
        self.assertEqual(code,200, 'Failed to get required vtt file for CORS testing. Got response %s from URL %s' % (code, url))

        # Check CORS headers
        self.assertTrue('Access-Control-Allow-Origin' in response.headers, 'Missing Access-Control-Allow-Origin header from %s' % url)
        self.assertEqual(response.headers['Access-Control-Allow-Origin'],"*", 'Expected header Access-Control-Allow-Origin:* but was Access-Control-Allow-Origin:%s' % (response.headers['Access-Control-Allow-Origin']))

        self.assertEqual(response.headers['Content-Type'],"text/vtt", 'Expected header Content-Type: text/vtt but was Content-Type: %s' % (response.headers['Content-Type']))

    def test_single_cors(self):
        url = "%s/%s" % (self.baseurl, 'api/cookbook/recipe/0003-mvm-video/manifest.json')

        response = requests.get(url, allow_redirects=False)
        code = response.status_code
        self.assertEqual(code,200, 'Failed to get required json file for CORS testing. Got response %s from URL %s' % (code, url))

        # Check CORS headers
        count = 0
        for header in response.headers.keys():
            if header == 'Access-Control-Allow-Origin':
                count += 1

        self.assertTrue('Access-Control-Allow-Origin' in response.headers, 'Missing Access-Control-Allow-Origin header from %s' % url)
        self.assertEqual(response.headers['Access-Control-Allow-Origin'],"*", 'Expected header Access-Control-Allow-Origin:* but was Access-Control-Allow-Origin:%s' % (response.headers['Access-Control-Allow-Origin']))

    def test_othercors(self):        
        url = "%s/%s" % (self.baseurl, 'api/cookbook/recipe/0009-book-1/manifest.json')

        response = requests.get(url, allow_redirects=False)
        code = response.status_code
        self.assertEqual(code,200, 'Failed to get required json file for CORS testing. Got response %s from URL %s' % (code, url))

        # Check CORS headers
        count = 0
        for header in response.headers.keys():
            if header == 'Access-Control-Allow-Origin':
                count += 1

        self.assertTrue('Access-Control-Allow-Origin' in response.headers, 'Missing Access-Control-Allow-Origin header from %s' % url)
        self.assertEqual(response.headers['Access-Control-Allow-Origin'],"*", 'Expected header Access-Control-Allow-Origin:* but was Access-Control-Allow-Origin:%s' % (response.headers['Access-Control-Allow-Origin']))



if __name__ == '__main__':
    os.environ["baseurl"] = 'http://localhost:9001'
    unittest.main()
