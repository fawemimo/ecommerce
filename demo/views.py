from itertools import product
from django.shortcuts import render
from inventory.models import *
from django.db.models import Count
from django.contrib.postgres.aggregates import ArrayAgg


def home(request):
    return render(request,'demo/index.html')

def category(request):
    data = Category.objects.all()
    context = {
        'data':data
    }
    return render(request,'demo/categories.html',context)

def product_by_category(request,category):
    data = Product.objects.filter(category__name=category).values('id','name','slug','category__name','product__store_price','product__product_inventory__units')
    context = {
        'data':data
    }
    return render(request, 'demo/product_by_category.html',context)


def product_detail(request,slug):

    filter_arguments = []

    if request.GET:
        for x in request.GET.values():
            filter_arguments.append(x)
        print('there are values')

        print(filter_arguments)
        data = ProductInventory.objects.filter(product__slug=slug).filter(attribute_values__attribute_value__in=filter_arguments).annotate(num_tags=Count('attribute_values')).filter(num_tags=len(filter_arguments)).values("id", "sku", "product__name", "store_price", "product_inventory__units").annotate(field_a=ArrayAgg("attribute_values__attribute_value"))
        print(data)    
    else:
        data = ProductInventory.objects.filter(product__slug=slug).filter(is_default=True).values(
        "id", "sku", "product__name", "store_price", "product_inventory__units").annotate(field_a=ArrayAgg("attribute_values__attribute_value"))
        print(data)
        
    y = ProductInventory.objects.filter(product__slug=slug).distinct().values(
    "attribute_values__product_attribute__name", "attribute_values__attribute_value")

    z = ProductTypeAttribute.objects.filter(product_type__product_type__product__slug=slug).distinct().values("product_attribute__name")
    
    context = {
        "data":data,
        "z":z,
        "y":y
    }
    return render(request,'demo/product_detail.html',context)