#!/usr/local/bin/python3
import unittest
import os
import sys
import requests

class TestPrezi3(unittest.TestCase):
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

    def test_prezi3(self):
        url = '%s/%s' % (self.baseurl, 'api/presentation/3.0/')
        self.checkOK(url, 'prezi3.iiif.io')


if __name__ == '__main__':
    baseurl = 'http://localhost:5000'
    if len(sys.argv) == 2:
        baseurl = sys.argv[1]

    os.environ["baseurl"] = baseurl
    os.environ["desturl"] = baseurl


    unittest.main()
