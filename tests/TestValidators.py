#!/usr/local/bin/python3.5
import unittest
import os
from urllib.request import urlopen
from urllib import request

class TestValidators(unittest.TestCase):
	baseurl = ''
	def setUp(self):
		self.baseurl = os.environ["baseurl"]
	def test_website(self):
		url = '%s/%s' % (self.baseurl, 'api/image/validator/service/list_tests')
		code = 0
		try:
			response=urlopen(url)
			code = response.code
		except request.HTTPError as error:	
			code = error.code
		self.assertEqual(code, 200, 'Problem retriving the image validator got: %s from %s' % (code, url))
		
	def test_api(self):
		url = '%s/%s' % (self.baseurl, 'api/presentation/validator/service')
		code = 0
		try:
			response=urlopen(url)
			code = response.code
		except request.HTTPError as error:	
			code = error.code
		self.assertEqual(code,200, 'Problem retriving the presentation validator got: %s from %s' % (code, url))

if __name__ == '__main__':
	unittest.main()
