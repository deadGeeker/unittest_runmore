import unittest


class Test_One(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("this is setup class method")

    def testBTwo(self):
        print("this is test two")

    @unittest.skip("skip testC")
    def testCThree(self):
        print("this is test three")

    def testAOne(self):
        print("this is test one")

    @classmethod
    def tearDownClass(cls):
        print("this is tear down method")


if __name__ == '__main__':
    unittest.main(verbosity=2)
