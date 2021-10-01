import unittest


def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    next


class MyFirstTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 2), 4)

    def test_substract(self):
        self.assertEqual(substract(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
    