#!/usr/local/bin/python3.5
import unittest
import os
import sys
import requests

class TestSharedCanvas(unittest.TestCase):
	baseurl = ''
	def setUp(self):
		self.baseurl = os.environ["baseurl"].replace('localhost','0.0.0.0')

	def checkRedirect(self, source, target):	
		code = 0
		response = requests.get(source, allow_redirects=False, headers={'host': 'shared-canvas.org'})
		code = response.status_code
		location = source
		if 'Location' in response.headers:
			location = response.headers['Location']
#		print(code, location)
		self.assertEqual(code, 302, 'Failed to get redirected to %s due to %s' % (source, code))
		self.assertEqual(location, target, 'Failed to redirect to the correct place. Expected %s but got %s' % (target, location))


	def test_root(self):
		url = '%s/%s' % (self.baseurl, '')
		dest = '%s/%s' % (self.baseurl, '/api/model/')
		self.checkRedirect(url, dest)

	def test_index(self):
		url = '%s/%s' % (self.baseurl, 'index.html')
		dest = '%s/%s' % (self.baseurl, '/api/model/')
		self.checkRedirect(url, dest)
	
if __name__ == '__main__':
	baseurl = 'http://localhost:5000'
	if len(sys.argv) == 2:
		baseurl = sys.argv[1]

	os.environ["baseurl"] = baseurl	


	unittest.main()
