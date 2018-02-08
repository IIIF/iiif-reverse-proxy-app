#!/usr/local/bin/python3
import unittest
import os
import sys
import requests
import json

class TestImageAPI(unittest.TestCase):
    baseurl = ''
    desturl = ''

    def setUp(self):
        self.baseurl = os.environ["baseurl"].replace('localhost','0.0.0.0')
        self.desturl = os.environ["desturl"].replace('localhost','0.0.0.0')

    def isValidJson(self, url):
        try:
            result = requests.get(url)
            result.json()
            self.assertEqual(result.status_code, 200, "Non 200 return code from %s" % url)
        except ValueError as error:
            self.assertTrue(False, "Invalid json from %s" % url)
        except requests.exceptions.ConnectionError as ConnectError:
            self.assertTrue(False, "Unable to connect to %s" % url)

    def test_10(self):
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/1.0/example/reference/detail/info.json'))
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/1.0/example/reference/67352ccc-d1b0-11e1-89ae-279075081939/info.json'))
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/1.0/example/reference/page1-full/info.json'))
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/1.0/example/reference/page2-full/info.json'))

    def test_11(self):
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/1.1/example/reference/detail/info.json'))
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/1.1/example/reference/67352ccc-d1b0-11e1-89ae-279075081939/info.json'))
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/1.1/example/reference/page1-full/info.json'))
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/1.1/example/reference/page2-full/info.json'))

    def test_20(self):
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/2.0/example/reference/detail/info.json'))
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/2.0/example/reference/67352ccc-d1b0-11e1-89ae-279075081939/info.json'))
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/2.0/example/reference/page1-full/info.json'))
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/2.0/example/reference/page2-full/info.json'))

    def test_21(self):
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/2.1/example/reference/detail/info.json'))
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/2.1/example/reference/67352ccc-d1b0-11e1-89ae-279075081939/info.json'))
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/2.1/example/reference/page1-full/info.json'))
        self.isValidJson('%s/%s' % (self.baseurl, 'api/image/2.1/example/reference/page2-full/info.json'))

if __name__ == '__main__':
    baseurl = 'http://localhost:5000'
    if len(sys.argv) == 2:
        baseurl = sys.argv[1]

    os.environ["baseurl"] = baseurl
    os.environ["desturl"] = baseurl


    unittest.main()
