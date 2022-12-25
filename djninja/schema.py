from typing import List
from inventory.models import *
from ninja import ModelSchema, Field


class CategorySchema(ModelSchema):
    class Config:
        model = Category
        model_fields = ["name", "slug"]


class ProductSchema(ModelSchema):
    class Config:
        model = Product
        model_fields = ["name", "web_id", "category"]


class BrandSchema(ModelSchema):
    class Config:
        model = Brand
        model_fields = ["name"]


class MediaSchema(ModelSchema):

    image: str

    class Config:
        model = Media
        model_fields = ["image", "alt_text"]


class ProductAttributeValueSchema(ModelSchema):
    class Config:
        model = ProductAttributeValue
        model_fields = "__all__"


class ProductTypeSchema(ModelSchema):
    class Config:
        model = ProductType
        model_fields = ["name"]


class InventorySchema(ModelSchema):

    brand: BrandSchema
    product: ProductSchema
    media: List[MediaSchema] = Field(alias="media_product_inventory")
    product_type: ProductTypeSchema
    attributes: List[ProductAttributeValueSchema] = Field(alias="")
    class Config:
        model = ProductInventory
        model_fields = ["id", "sku", "brand", "product"]
