#!/usr/local/bin/python3.5
import unittest
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
from urllib import request
import os
import json

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

	def test_cookbook_manifest(self):
		url = '%s/%s' % (self.baseurl, 'api/cookbook/recipe/0057-publishing-v2-and-v3/manifest.json')
		print (url)
		with urlopen(url) as urlPointer:
			manifest = json.loads(urlPointer.read().decode())
			self.assertEqual(manifest['@context'], 'http://iiif.io/api/presentation/3/context.json', 'Expected default retrieval of manifest to be version 3')

		opener = request.build_opener()
		opener.addheaders = [('Accept', "application/ld+json;profile=http://iiif.io/api/presentation/3/context.json")]
		with opener.open(url) as urlPointer:
			manifest = json.loads(urlPointer.read().decode())
			self.assertEquals(manifest['@context'], 'http://iiif.io/api/presentation/3/context.json', 'Passing the 3 accept header should get version 3 but got version 2')

		opener = request.build_opener()
		opener.addheaders = [('Accept', "application/ld+json;profile=http://iiif.io/api/presentation/2/context.json")]
		with opener.open(url) as urlPointer:
			manifest = json.loads(urlPointer.read().decode())
			self.assertEquals(manifest['@context'], 'http://iiif.io/api/presentation/2/context.json', 'Passing the 2 accept header should get version 2 manifest')
                

if __name__ == '__main__':
	unittest.main()
