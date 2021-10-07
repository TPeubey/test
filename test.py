import unittest


def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x/y


def first(x):
    return x


class MyFirstTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 2), 4)

    def test_substract(self):
        self.assertEqual(substract(2, 2), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(divide(16, 4), 4)

    def test_first(self):
        self.assertEqual(first("First test"), "First test")
        self.assertIn(first("First"), "First test")


if __name__ == '__main__':
    unittest.main()
