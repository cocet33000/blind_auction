from dotenv import load_dotenv
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class Item(Model):
    """_summary_
    Args:
        Model (_type_): _description_
    """
    class Meta:
        """_summary_
        """
        load_dotenv()
        host = "http://localhost:8000"
        table_name = "blind_auction_items"
        region = 'ap-northeast-1'

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()
