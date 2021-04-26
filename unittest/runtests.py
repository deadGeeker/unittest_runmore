import unittest
from HTMLTestRunner import HTMLTestRunner


find = unittest.defaultTestLoader.discover("tests/", pattern="test*.py")
filename = "report/report.html"
fp = open(filename, 'wb')

runner = HTMLTestRunner(stream=fp, title='AutoTest', description='My Selenium auto test')
runner.run(find)
fp.close()
