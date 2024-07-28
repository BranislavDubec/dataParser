from rest_framework import serializers
from .models import AttributeName, AttributeValue, Attribute, Product, ProductAttributes, Image, ProductImage, Catalog

class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeName
        fields = '__all__'
    
    def validate(self, data):
        unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
        if unknown_keys:
            raise serializers.ValidationError("Uknown fields detected: {}".format(unknown_keys))
        return data

class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = '__all__'
    def validate(self, data):
        unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
        if unknown_keys:
            raise serializers.ValidationError("Uknown fields detected: {}".format(unknown_keys))
        return data
    
class AttributeSerializer(serializers.ModelSerializer):
    nazev_atributu_id = serializers.PrimaryKeyRelatedField(queryset=AttributeName.objects.all())
    hodnota_atributu_id = serializers.PrimaryKeyRelatedField(queryset=AttributeValue.objects.all())
    
    class Meta:
        model = Attribute
        fields = '__all__'

    def validate(self, data):
        unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
        if unknown_keys:
            raise serializers.ValidationError("Uknown fields detected: {}".format(unknown_keys))
        return data
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
        if unknown_keys:
            raise serializers.ValidationError("Uknown fields detected: {}".format(unknown_keys))
        return data
    

class ProductAttributesSerializer(serializers.ModelSerializer):
    attribute = serializers.PrimaryKeyRelatedField(queryset=Attribute.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = ProductAttributes
        fields = '__all__'

    def validate(self, data):
        unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
        if unknown_keys:
            raise serializers.ValidationError("Uknown fields detected: {}".format(unknown_keys))
        return data
    

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

    def validate(self, data):
        unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
        if unknown_keys:
            raise serializers.ValidationError("Uknown fields detected: {}".format(unknown_keys))
        return data
    

class ProductImageSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    obrazek_id = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all())

    class Meta:
        model = ProductImage
        fields = '__all__'
    
    def validate(self, data):
        unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
        if unknown_keys:
            raise serializers.ValidationError("Uknown fields detected: {}".format(unknown_keys))
        return data
    

class CatalogSerializer(serializers.ModelSerializer):
    products_ids = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, required=False)
    attributes_ids = serializers.PrimaryKeyRelatedField(queryset=Attribute.objects.all(), many=True, required=False)

    class Meta:
        model = Catalog
        fields = '__all__'
    
    def validate(self, data):
        unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
        if unknown_keys:
            raise serializers.ValidationError("Uknown fields detected: {}".format(unknown_keys))
        return data
    