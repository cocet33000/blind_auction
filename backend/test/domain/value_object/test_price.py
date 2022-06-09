import unittest

from main.domain.value_object.price import Price


class TestPrice(unittest.TestCase):
    def test_Price型に負の値はNG(self):
        with self.assertRaises(ValueError):
            Price(-100)


if __name__ == "__main__":
    unittest.main()
