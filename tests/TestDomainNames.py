import unittest
import os
import sys
import requests

class TestDomainNames(unittest.TestCase):
    baseurl = ''
    desturl = ''
    def setUp(self):
        self.baseurl = os.environ["baseurl"].replace('localhost','0.0.0.0')
        self.desturl = os.environ["desturl"].replace('localhost','0.0.0.0')

    def checkOK(self, source, host):
        code = 0
        response = requests.get(source, allow_redirects=False, headers={'host': host})
        code = response.status_code
        self.assertEqual(code, 200, 'Failed to get 200 from host %s due to %s' % (host, code))

    def redirectCheck(self, url, target, host):
        code = 0
        response = requests.get(url, allow_redirects=False, headers={'host': host})
        code = response.status_code
        location = url
        if 'Location' in response.headers:
            location = response.headers['Location']

        self.assertEqual(code, 301, 'Failed to get redirected to %s due to %s' % (url, code))
        self.assertEqual(location, target, 'Failed to redirect to the correct place. Expected %s but got %s' % (target, location))

    def runShowcaseCheck(self, host):     
        url = '%s/%s' % (self.baseurl, '')
        target = 'https://iiif.io/demos/'
        self.redirectCheck(url, target, host)

        url = '%s/%s' % (self.baseurl, '/showcase/osd-viewer/')
        target = 'https://iiif.io/demos/'
        self.redirectCheck(url, target, host)


    def test_showcase(self):
        self.runShowcaseCheck('showcase.iiif.io')

    def test_demo(self):
        self.runShowcaseCheck('demo.iiif.io')
 
    def test_demos(self):
        self.runShowcaseCheck('demos.iiif.io')

if __name__ == '__main__':
    baseurl = 'http://localhost:9001'
    if len(sys.argv) == 2:
        baseurl = sys.argv[1]

    os.environ["baseurl"] = baseurl
    os.environ["desturl"] = baseurl

    unittest.main()
