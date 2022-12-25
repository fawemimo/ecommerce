from ninja import NinjaAPI
from .schema import *
from typing import List

api = NinjaAPI()


@api.get("inventory/category/all", response=List[CategorySchema])
def category_list(request):
    queries = Category.objects.all()
    return queries


@api.get(
    "inventory/products/category/{category_slug}/",
    response=List[ProductSchema],
)
def category_list(request, category_slug: str):
    queries = Product.objects.filter(category__slug=category_slug)
    return queries


@api.get("inventory/{web_id}/", response=List[InventorySchema])
def inventory_list(request, web_id: str):
    qs = ProductInventory.objects.filter(product__web_id=web_id)
    return qs
