import unittest


class Test_Two(unittest.TestCase):

    def add(self):
        self.assertEqual((1 + 2), 3)
        print("add passed")

    def multiply(self):
        self.assertEqual((1 * 2), 2)
        print("multi passed")


if __name__ == '__main__':
    unittest.main()
