import unittest

def check(x):
    return x >= 100

class MyTest(unittest.TestCase):
    def test(self):
        self.assertTrue(check(420))

if __name__ == '__main__':
    unittest.main()
