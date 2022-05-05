import unittest
from Model.Item import Item


class TestItemModel(unittest.TestCase):
    def test_itemモデルを作成(self):

        self.assertEqual("foo".upper(), "FOO")


if __name__ == "__main__":
    unittest.main()
