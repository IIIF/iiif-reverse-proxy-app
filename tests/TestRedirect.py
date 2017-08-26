#!/usr/local/bin/python3.5
import unittest
import os
import sys
import requests

class TestRedirect(unittest.TestCase):
	baseurl = ''
	def setUp(self):
		self.baseurl = os.environ["baseurl"]

	def checkRedirect(self, source, target):	
		code = 0
		response = requests.get(source, allow_redirects=False)
		code = response.status_code
		location = source
		if 'Location' in response.headers:
			location = response.headers['Location']
#		print(code, location)
		self.assertEqual(code, 302, 'Failed to get redirected to %s due to %s' % (source, code))
		self.assertEqual(location, target, 'Failed to redirect to the correct place. Expected %s but got %s' % (target, location))


	def test_image(self):
		url = '%s/%s' % (self.baseurl, 'api/image/')
		dest = '%s/%s' % (self.baseurl, 'api/image/2.1/')
		self.checkRedirect(url, dest)

	def test_presentation(self):
		url = '%s/%s' % (self.baseurl, 'api/presentation/index.html')
		dest = '%s/%s' % (self.baseurl, 'api/presentation/2.1/')
		self.checkRedirect(url, dest)
	def test_validator(self):
		url = '%s/%s' % (self.baseurl, 'api/presentation/validator')
		dest = '%s/%s' % (self.baseurl, 'api/presentation/validator/service')
		self.checkRedirect(url, dest)
	# why is this here?	
	def test_ontology(self):
		url = '%s/%s' % (self.baseurl, 'api/presentation/2')
		dest = '%s/%s' % (self.baseurl, 'api/presentation/2/ontology.xml')
		self.checkRedirect(url, dest)
	def test_metadata(self):
		url = '%s/%s' % (self.baseurl, 'api/metadata')
		dest = '%s/%s' % (self.baseurl, 'api/presentation/2.1/')
		self.checkRedirect(url, dest)
	def test_presentation1(self):
		url = '%s/%s' % (self.baseurl, '/api/presentation/1.0')
		dest = '%s/%s' % (self.baseurl, 'api/presentation/2.1/')
		self.checkRedirect(url, dest)
	def test_auth(self):
		url = '%s/%s' % (self.baseurl, '/api/auth/')
		dest = '%s/%s' % (self.baseurl, 'api/auth/1.0/')
		self.checkRedirect(url, dest)
	def test_auth0(self):
		url = '%s/%s' % (self.baseurl, '/api/auth/0/')
		dest = '%s/%s' % (self.baseurl, 'api/auth/1.0/')
		self.checkRedirect(url, dest)
	def test_search(self):
		url = '%s/%s' % (self.baseurl, '/api/search')
		dest = '%s/%s' % (self.baseurl, 'api/search/1.0/')
		self.checkRedirect(url, dest)

	
if __name__ == '__main__':
	baseurl = 'http://localhost:5000'
	if len(sys.argv) == 2:
		baseurl = sys.argv[1]

	os.environ["baseurl"] = baseurl	


	unittest.main()