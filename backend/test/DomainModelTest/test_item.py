import unittest
import datetime
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent / "main"))
from DomainModel import Item


class TestItemModel(unittest.TestCase):
    def test_input_valid_parameter(self):

        input_param_list = [
            (1, "hoge", "test/testimg.png", "hoge", 0, 0),
            (99999999, "hoge", "test/testimg.png", "hoge", 0, 0),
            (1, "hoge", "test/testimg.png", "hoge", 999999, 0),
            (1, "hoge", "test/testimg.png", "hoge", 0, 99999999),
        ]
        for ITEM_ID, ITEM_NAME, ITEM_IMAGE_SRC, DESCRIPTION, START_PRICE, BID_NUM in input_param_list:
            with self.subTest(
                            ITEM_ID=ITEM_ID, 
                            ITEM_NAME=ITEM_NAME,  
                            ITEM_IMAGE_SRC=ITEM_IMAGE_SRC, 
                            DESCRIPTION=DESCRIPTION, 
                            START_PRICE=START_PRICE, 
                            BID_NUM=BID_NUM, 
                            ):
                item = Item(
                    id = ITEM_ID,
                    name = ITEM_NAME,
                    image_src = ITEM_IMAGE_SRC,
                    description = DESCRIPTION,
                    start_price = START_PRICE,
                    bid_num = BID_NUM,
                )

                self.assertEqual(item.id, ITEM_ID)
                self.assertEqual(item.name, ITEM_NAME)
                self.assertEqual(item.image_src, ITEM_IMAGE_SRC)
                self.assertEqual(item.description, DESCRIPTION)
                self.assertEqual(item.start_price, START_PRICE)
                self.assertEqual(item.bid_num, BID_NUM)


    def test_input_invalid_parameter_except_TypeError(self):
        input_param_list = [
            ("aaa", "hoge", "test/testimg.png", "hoge", 0, 0),
            (1, 1, "test/testimg.png", "hoge", 0, 0),
            (1, "hoge", 1, "hoge", 0, 0),
            (1, "hoge", "test/testimg.png", 1, 0, 0),
            (1, "hoge", "test/testimg.png", "hoge", "aaa", 0),
            (1, "hoge", "test/testimg.png", "hoge", 0, "aaa"),
        ]
        for ITEM_ID, ITEM_NAME, ITEM_IMAGE_SRC, DESCRIPTION, START_PRICE, BID_NUM in input_param_list:
            with self.subTest(
                            ITEM_ID=ITEM_ID, 
                            ITEM_NAME=ITEM_NAME,  
                            ITEM_IMAGE_SRC=ITEM_IMAGE_SRC, 
                            DESCRIPTION=DESCRIPTION, 
                            START_PRICE=START_PRICE, 
                            BID_NUM=BID_NUM, 
                            ):
                with self.assertRaises(TypeError):
                    item = Item(
                        id = ITEM_ID,
                        name = ITEM_NAME,
                        image_src = ITEM_IMAGE_SRC,
                        description = DESCRIPTION,
                        start_price = START_PRICE,
                        bid_num = BID_NUM,
                    )


    def test_input_invalid_parameter_except_ValueError(self):
        input_param_list = [
            (-1, "hoge", "test/testimg.png", "hoge", 0, 0),
            (0, "hoge", "test/testimg.png", "hoge", 0, 0),
            (100000000, "hoge", "test/testimg.png", "hoge", 0, 0),
            (1, "hoge", "test/testimg.png", "hoge", -1, 0),
            (1, "hoge", "test/testimg.png", "hoge", 1000000, 0),
            (1, "hoge", "test/testimg.png", "hoge", 0, -1),
            (1, "hoge", "test/testimg.png", "hoge", 0, 100000000),
        ]
        for ITEM_ID, ITEM_NAME, ITEM_IMAGE_SRC, DESCRIPTION, START_PRICE, BID_NUM in input_param_list:
            with self.subTest(
                ITEM_ID=ITEM_ID, 
                ITEM_NAME=ITEM_NAME,  
                ITEM_IMAGE_SRC=ITEM_IMAGE_SRC, 
                DESCRIPTION=DESCRIPTION, 
                START_PRICE=START_PRICE, 
                BID_NUM=BID_NUM, 
            ):
                with self.assertRaises(ValueError):
                    item = Item(
                        id = ITEM_ID,
                        name = ITEM_NAME,
                        image_src = ITEM_IMAGE_SRC,
                        description = DESCRIPTION,
                        start_price = START_PRICE,
                        bid_num = BID_NUM,
                    )


if __name__ == "__main__":
    unittest.main()
