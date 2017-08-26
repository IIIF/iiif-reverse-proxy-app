#!/usr/local/bin/python3.5
import unittest
import TestJsonLD
import TestProxy
import TestRedirect
import TestCommingsoon
import TestValidators
import os
import sys

def suite():
	tests = []
	tests.append(unittest.TestLoader().loadTestsFromTestCase(TestJsonLD.TestJsonLD))
	tests.append(unittest.TestLoader().loadTestsFromTestCase(TestProxy.TestProxy))
	tests.append(unittest.TestLoader().loadTestsFromTestCase(TestRedirect.TestRedirect))
	tests.append(unittest.TestLoader().loadTestsFromTestCase(TestCommingsoon.TestCommingsoon))
	tests.append(unittest.TestLoader().loadTestsFromTestCase(TestValidators.TestValidators))
	return  unittest.TestSuite(tests)

baseurl = 'http://localhost:5000'
if len(sys.argv) == 2:
	baseurl = sys.argv[1]

os.environ["baseurl"] = baseurl	

mySuit=suite()

runner=unittest.TextTestRunner()
runner.run(mySuit)
