import unittest

find = unittest.defaultTestLoader.discover("tests/", pattern="test*.py")
runner = unittest.TextTestRunner()
runner.run(find)