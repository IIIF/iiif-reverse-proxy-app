#!/usr/local/bin/python3.5
import unittest
import os
import sys
import requests
try:
    import urlparse
except:
    from urllib.parse import urlparse

class TestSharedCanvas(unittest.TestCase):
    baseurl = ''
    desturl = ''
    def setUp(self):
        self.baseurl = os.environ["baseurl"]
        self.desturl = os.environ["desturl"]

    def checkOK(self,url):
        code = 0
        response = requests.get(url, allow_redirects=False)
        code = response.status_code
        self.assertEqual(code, 200, 'Failed to get 200 from host %s due to %s' % (url, code))
    
    def test_checkPage(self):
        url = '{}/{}'.format(self.baseurl, 'api/model/shared-canvas/1.0/')
        self.checkOK(url)

if __name__ == '__main__':
    baseurl = 'http://localhost:9001'
    if len(sys.argv) == 2:
        baseurl = sys.argv[1]

    os.environ["baseurl"] = baseurl
    os.environ["desturl"] = baseurl


    unittest.main()
    
