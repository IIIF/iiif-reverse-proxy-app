#!/usr/local/bin/python3.5
import unittest
from urllib.request import urlopen
from urllib import request
import os

class TestJsonLD(unittest.TestCase):
	baseurl = ''
	def setUp(self):
		self.baseurl = os.environ["baseurl"]

	def test_mimetype(self):
		url = '%s/%s' % (self.baseurl, 'api/image/2/context.json')
		response=urlopen(url)
		mimetype=response.info().get('Content-type')
		self.assertEqual(mimetype, 'application/json', 'Mimetype should be json if I dont support jsonld')
		
	def test_jsonldmimetype(self):
		url = '%s/%s' % (self.baseurl, 'api/image/2/context.json')
		jsonldmimetype='application/ld+json'
		opener = request.build_opener()
		opener.addheaders = [('Accept', jsonldmimetype)]
		response=opener.open(url)
		mimetype=response.info().get('Content-type')
		self.assertEqual(mimetype, 'application/ld+json', 'Mimetype should be jsonld if I support jsonld')

if __name__ == '__main__':
	unittest.main()
