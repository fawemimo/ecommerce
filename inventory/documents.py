from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import ProductInventory

@registry.register_document
class ProductInventoryDocument(Document):

    product = fields.ObjectField(
        properties={
            "name": fields.TextField()
        }
    )
    
    product_inventory = fields.ObjectField(
        properties={
            "units": fields.IntegerField(),
        }
    )

    class Index:
        name = "productinventory"

    class Django:
        model = ProductInventory

        fields = ["id", "sku",]

# py manage.py search_index --rebuild 

# curl -X GET "localhost:9200/productinventory/_doc/1?pretty"