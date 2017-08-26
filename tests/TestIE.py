#!/usr/local/bin/python3.5
import unittest
from urllib.request import urlopen
from urllib import request
import os

class TestIE(unittest.TestCase):
	baseurl = ''
	def setUp(self):
		self.baseurl = os.environ["baseurl"]

	def test_ieheader(self):
		url = '%s/%s' % (self.baseurl, 'index.html')
		response=urlopen(url)
		ieHeader=response.info().get('X-UA-Compatible')
		self.assertEqual(ieHeader, 'IE=Edge,chrome=1', 'Missing IE header')
		
if __name__ == '__main__':
	unittest.main()
