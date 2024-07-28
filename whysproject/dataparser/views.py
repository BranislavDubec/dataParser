from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db import transaction
from .models import AttributeName, AttributeValue, Attribute, Product, ProductAttributes, Image, ProductImage, Catalog
from .serializers import (AttributeNameSerializer, AttributeValueSerializer, AttributeSerializer, ProductSerializer, 
                          ProductAttributesSerializer, ImageSerializer, ProductImageSerializer, CatalogSerializer)

import json

model_mapping = {
    'AttributeName': (AttributeName, AttributeNameSerializer),
    'AttributeValue': (AttributeValue, AttributeValueSerializer),
    'Attribute': (Attribute, AttributeSerializer),
    'Product': (Product, ProductSerializer),
    'ProductAttributes': (ProductAttributes, ProductAttributesSerializer),
    'Image': (Image, ImageSerializer),
    'ProductImage': (ProductImage, ProductImageSerializer),
    'Catalog': (Catalog, CatalogSerializer)
}


@api_view(['POST'])
@transaction.atomic
def import_data(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return Response("Error: Wrong Json Data", status=status.HTTP_400_BAD_REQUEST)
    try:
        with transaction.atomic():
            for item in data:
                for model_name, model_data in item.items():
                    model_class, model_serializer = model_mapping.get(model_name, None)
                    if not model_class:
                        return Response("Wrong model", status=status.HTTP_400_BAD_REQUEST)
                    if 'id' not in model_data:
                        return Response("Wrong model", status=status.HTTP_400_BAD_REQUEST)
                    instance = model_class.objects.filter(id=model_data['id']).first()
                    if instance:
                        serializer = model_serializer(instance, data=model_data)
                    else: 
                        serializer = model_serializer(data=model_data)

                    if serializer.is_valid():
                        serializer.save()
                    else:
                        raise Exception(serializer.errors)
    except Exception as e:
        return Response("Error: Wrong Json Data", status=status.HTTP_400_BAD_REQUEST)
    return Response("Data saved succesfully", status=status.HTTP_200_OK)

@api_view(['GET'])
def attribute_name_data(request):
    attributeNames = AttributeName.objects.all()
    serializer = AttributeNameSerializer(attributeNames, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def attribute_value_data(request):
    attributeValues = AttributeValue.objects.all()
    serializer = AttributeValueSerializer(attributeValues, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def attribute_data(request):
    attributes = Attribute.objects.all()
    serializer = AttributeSerializer(attributes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_data(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_attributes_data(request):
    productAttributes = ProductAttributes.objects.all()
    serializer = ProductAttributesSerializer(productAttributes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def image_data(request):
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_image_data(request):
    productImages = ProductImage.objects.all()
    serializer = ProductImageSerializer(productImages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def catalog_data(request):
    catalogs = Catalog.objects.all()
    serializer = CatalogSerializer(catalogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def attribute_name_detail(request, id):
    try:
        attribute_name = AttributeName.objects.get(id=id)
    except AttributeName.DoesNotExist:
        return Response("No data", status=status.HTTP_404_NOT_FOUND)
    serializer = AttributeNameSerializer(attribute_name)
    return Response(serializer.data)

@api_view(['GET'])
def attribute_value_detail(request, id):
    try:
        attributeValue = AttributeValue.objects.get(id=id)
    except AttributeValue.DoesNotExist:
        return Response("No data", status=status.HTTP_404_NOT_FOUND)
    serializer = AttributeValueSerializer(attributeValue)
    return Response(serializer.data)

@api_view(['GET'])
def attribute_detail(request, id):
    try:
        attribute = Attribute.objects.get(id=id)
    except Attribute.DoesNotExist:
        return Response("No data", status=status.HTTP_404_NOT_FOUND)
    serializer = AttributeSerializer(attribute)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response("No data", status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def product_attributes_detail(request, id):
    try:
        productAttributes = ProductAttributes.objects.get(id=id)
    except ProductAttributes.DoesNotExist:
        return Response("No data", status=status.HTTP_404_NOT_FOUND)
    serializer = ProductAttributesSerializer(productAttributes)
    return Response(serializer.data)

@api_view(['GET'])
def image_detail(request, id):
    try:
        image = Image.objects.get(id=id)
    except Image.DoesNotExist:
        return Response("No data", status=status.HTTP_404_NOT_FOUND)
    serializer = ImageSerializer(image)
    return Response(serializer.data)

@api_view(['GET'])
def product_image_detail(request, id):
    try:
        productImage = ProductImage.objects.get(id=id)
    except ProductImage.DoesNotExist:
        return Response("No data", status=status.HTTP_404_NOT_FOUND)
    serializer = ProductImageSerializer(productImage)
    return Response(serializer.data)

@api_view(['GET'])
def catalog_detail(request, id):
    try:
        catalog = Catalog.objects.get(id=id)
    except Catalog.DoesNotExist:
        return Response("No data", status=status.HTTP_404_NOT_FOUND)
    serializer = CatalogSerializer(catalog)
    return Response(serializer.data)