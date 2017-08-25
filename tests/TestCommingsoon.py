#!/usr/local/bin/python3.5
import unittest
import os
import sys
import requests

class TestCommingsoon(unittest.TestCase):
	baseurl = ''
	def setUp(self):
		self.baseurl = os.environ["baseurl"].replace('localhost','0.0.0.0')

	def checkRedirect(self, source, target, host):	
		code = 0
		response = requests.get(source, allow_redirects=False, headers={'host': host})
		code = response.status_code
		location = source
		if 'Location' in response.headers:
			location = response.headers['Location']
#		print(code, location)
		self.assertEqual(code, 302, 'Failed to get redirected to %s due to %s' % (source, code))
		self.assertEqual(location, target, 'Failed to redirect to the correct place. Expected %s but got %s' % (target, location))


	def test_example(self):
		url = '%s/%s' % (self.baseurl, 'api/image/2.0/example/reference/67352ccc-d1b0-11e1-89ae-279075081939/info.json')
		dest = '%s/%s' % (self.baseurl, 'commingsoon.html')
		self.checkRedirect(url, dest, 'iiif.io')

	def test_index(self):
		url = '%s/%s' % (self.baseurl, 'shims/wales/potter/1861-01-02.json')
		dest = '%s/%s' % (self.baseurl, 'commingsoon.html')
		self.checkRedirect(url, dest, 'showcase.iiif.io')
	
if __name__ == '__main__':
	baseurl = 'http://localhost:5000'
	if len(sys.argv) == 2:
		baseurl = sys.argv[1]

	os.environ["baseurl"] = baseurl	


	unittest.main()
