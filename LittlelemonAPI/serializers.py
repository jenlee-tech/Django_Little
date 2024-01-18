from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal
from .models import Category
# another example


class CategoryItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug', 'title', 'id']

# added HyperlinkedModelSerializer


class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    # price = serializers.DecimalField(
    # max_digits=6, decimal_places=2, min_value=2)
    price_after_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    # category = serializers.StringRelatedField()
    category = CategoryItemsSerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    # category = serializers.HyperlinkedRelatedField(
    #     queryset=Category.objects.all(),
    #     view_name='category-detail'
    # )

    def validate_price(self, value):
        if (value < 2):
            raise serializers.ValidationError(
                'Hello !!! Price should not be less than 2.0')

    def validate_stock(self, value):
        if (value < 0):
            raise serializers.ValidationError('Stock cannot be negative')

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock',
                  'price_after_tax', 'category', 'category_id']
        depth = 1
        # extra_kwargs = {
        #     'price': {'min_value': 2},
        #     'stock': {'source': 'inventory', 'min_value': 0}
        # }

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)


# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     inventory = serializers.IntegerField()
