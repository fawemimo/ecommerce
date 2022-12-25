from rest_framework import serializers
from inventory.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "web_id"]
        read_only = True
        editable = False


class CategorySerializer(serializers.ModelSerializer):
    '''
        Category serializer
    '''
    class Meta:
        model = Category
        fields = ('name','slug',)
        read_only = True


class AllProducts(serializers.ModelSerializer):
    '''
        Product database for frontend developers and all the fields were defined,
        It can be read and is not allow to edit or update to the database
    '''
    class Meta:
        model = Product
        fields = "__all__"
        read_only = True
        editable = False


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('name',)


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        exclude  = ['id']
        depth = 2


class MediaSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Media 
        fields = ['image','alt_text']
        read_only = True

    def get_image(self,obj):
        return self.context['request'].build_absolute_uri(obj.image.url)


class ProductSerializer(serializers.ModelSerializer):

    # category = CategorySerializer(many=True)
    
    class Meta:
        model = Product
        fields = ('name',)
        read_only = True
        editable = False

class ProductInventorySerializer(serializers.ModelSerializer) :
    # brand     = BrandSerializer(
    #     many=False,
    #     read_only=True
    # )
    # attribute_values = ProductAttributeValueSerializer(
        
    #     many = True,

    # )
    # media = MediaSerializer(
    #     source = 'media_product_inventory',
    #     many = True,
    # )

    product = ProductSerializer(many=False,read_only=True)

    class Meta:
        model = ProductInventory
        fields = [
            'sku',
            # 'media',
            'store_price',
            'is_default',
            'product',
            # 'product_type',
            # 'brand',
            # 'attribute_values'
        ]
        read_only = True