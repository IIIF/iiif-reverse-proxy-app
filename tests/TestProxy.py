#!/usr/local/bin/python3.5
import unittest
import os
from urllib.request import urlopen
from urllib import request

class TestProxy(unittest.TestCase):
	baseurl = ''
	def setUp(self):
		self.baseurl = os.environ["baseurl"]
	def test_website(self):
		url = '%s/%s' % (self.baseurl, 'technical-details/index.html')
		code = 0
		try:
			response=urlopen(url)
			code = response.code
		except request.HTTPError as error:	
			code = error.code
		self.assertEqual(code,200, 'Problem retriving the main website got: %s from %s' % (code, url))
		
	def test_api(self):
		url = '%s/%s' % (self.baseurl, 'api/index.html')
		code = 0
		try:
			response=urlopen(url)
			code = response.code
		except request.HTTPError as error:	
			code = error.code
		self.assertEqual(code,200, 'Problem retriving the api website fot: %s from %s' % (code, url))

if __name__ == '__main__':
	unittest.main()
