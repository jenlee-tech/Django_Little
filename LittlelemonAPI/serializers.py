from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal
from .models import Category
# another example


class CategoryItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug', 'title', 'id']


class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    stock = serializers.IntegerField(source='inventory')

    price_after_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    # category = serializers.StringRelatedField()
    # category = CategoryItemsSerializer()
    # category = serializers.HyperlinkedRelatedField(
    #     queryset=Category.objects.all(),
    #     view_name='category-detail'
    # )

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock',
                  'price_after_tax', 'category']
        depth = 1

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)


# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     inventory = serializers.IntegerField()