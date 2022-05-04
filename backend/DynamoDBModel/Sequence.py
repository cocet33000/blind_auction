from dotenv import load_dotenv
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from pynamodb.attributes import NumberAttribute


class Sequence(Model):
    class Meta:
        load_dotenv()
        host = "http://localhost:8000"
        table_name = "blind_auction_sequence"
        region = "ap-northeast-1"

    table_name = UnicodeAttribute(hash_key=True)
    current_number = NumberAttribute(null=False)
