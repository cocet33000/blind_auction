import os

from dotenv import load_dotenv
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from pynamodb.attributes import NumberAttribute


class Sequence(Model):
    class Meta:
        load_dotenv()
        if os.environ.get("MODE") == "local":
            host = "http://localhost:8000"
        table_name = os.environ.get("AWS_DYNAMO_DB_SEQUENCE_TABLE_NAME")
        region = "ap-northeast-1"

    table_name = UnicodeAttribute(hash_key=True)
    current_number = NumberAttribute(null=False)
