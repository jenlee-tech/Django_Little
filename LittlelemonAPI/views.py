from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem, Category
from .serializers import MenuItemSerializer
from .serializers import CategoryItemsSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.
# # using generic view classes of drf

# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer


# class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serialize_category = CategoryItemsSerializer(category)
    return Response(serialize_category.data)


class CategoryItemsView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryItemsSerializer


@api_view()
def menu_items(request):
    items = MenuItem.objects.select_related('category').all()
    # serialized_item = MenuItemSerializer(items, many=True)
    serialized_item = MenuItemSerializer(
        items, many=True, context={'request': request})
    return Response(serialized_item.data)


@api_view()
def single_item(request, id):
    # item = MenuItem.objects.get(pk=id) - below line is cooler
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)
