#!/usr/local/bin/python3.5
import unittest
import os
from urllib.request import urlopen
from urllib import request
import requests

class TestValidators(unittest.TestCase):
    baseurl = ''
    def setUp(self):
        self.baseurl = os.environ["baseurl"]

    def test_imagevalidator(self):
        url = '%s/%s' % (self.baseurl, 'api/image/validator/service/list_tests')
        code = 0
        try:
            response = requests.get(url, allow_redirects=False)
            code = response.status_code
        except request.HTTPError as error:	
            code = error.code

        self.assertEqual(code, 302, 'Problem retriving the image validator got: %s from %s' % (code, url))

        if 'Location' in response.headers:
            location = response.headers['Location']
		
        self.assertEqual(location, 'https://image-validator.iiif.io/list_tests', "Redirect target incorrect")
        ## TODO test webp

    def test_api(self):
        url = '%s/%s' % (self.baseurl, 'api/presentation/validator/service/validate')
        code = 0
        try:
            response = requests.get(url, allow_redirects=False)
            code = response.status_code
        except request.HTTPError as error:	
            code = error.code

        self.assertEqual(code,302, 'Problem retriving the presentation validator got: %s from %s' % (code, url))

        if 'Location' in response.headers:
            location = response.headers['Location']

        self.assertEqual(location, 'https://presentation-validator.iiif.io/validate', "Redirect target incorrect")

if __name__ == '__main__':
	unittest.main()
