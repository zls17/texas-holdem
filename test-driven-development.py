import unittest

def product(a, b):
    return a * b


class TestProduct(unittest.TestCase):
    def test_multiply_two_numbers(self):
        self.assertEqual(
            product(3, 5),
            15
        )

if __name__ == "__main__":
    unittest.main()