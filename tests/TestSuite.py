#!/usr/local/bin/python3
import unittest
import TestJsonLD
import TestProxy
import TestRedirect
import TestComingsoon
import TestRDFXML
import TestValidators
import TestIE
import TestPrezi3
import TestImageAPI
import TestHttps
import TestCORS
import os
import sys

def suite():
    tests = []
    tests.append(unittest.TestLoader().loadTestsFromTestCase(TestJsonLD.TestJsonLD))
    tests.append(unittest.TestLoader().loadTestsFromTestCase(TestProxy.TestProxy))
    tests.append(unittest.TestLoader().loadTestsFromTestCase(TestRedirect.TestRedirect))
    tests.append(unittest.TestLoader().loadTestsFromTestCase(TestValidators.TestValidators))
    tests.append(unittest.TestLoader().loadTestsFromTestCase(TestIE.TestIE))
    tests.append(unittest.TestLoader().loadTestsFromTestCase(TestRDFXML.TestRDFXML))
    tests.append(unittest.TestLoader().loadTestsFromTestCase(TestPrezi3.TestPrezi3))
    tests.append(unittest.TestLoader().loadTestsFromTestCase(TestHttps.TestHttps))
    tests.append(unittest.TestLoader().loadTestsFromTestCase(TestImageAPI.TestImageAPI))
    tests.append(unittest.TestLoader().loadTestsFromTestCase(TestCORS.TestCORS))
    return  unittest.TestSuite(tests)

if __name__ == '__main__':
    baseurl = 'http://localhost:9001'
    desturl = baseurl
    if len(sys.argv) > 1:
        baseurl = sys.argv[1]
        desturl = baseurl
        if len(sys.argv) > 2:
            desturl = sys.argv[2]

    os.environ["baseurl"] = baseurl
    os.environ["desturl"] = desturl

    mySuit=suite()

    runner=unittest.TextTestRunner()
    result = runner.run(mySuit)

    if result.wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(1)
        
