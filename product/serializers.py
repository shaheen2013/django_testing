from rest_framework import serializers
from .models import Product, Variant
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):  # create class to serializer user model
    # variants = serializers.PrimaryKeyRelatedField(many=True, queryset=Variant.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'klass', 'image', 'status')

    def to_representation(self, instance):
        data = super(ProductSerializer, self).to_representation(instance)
        data.update({"variants": instance.variants.values("title", "available_stock")})
        return data


class ProductListSerializer(serializers.ModelSerializer):  # create class to serializer user model
    # variants = serializers.PrimaryKeyRelatedField(many=True, queryset=Variant.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'status')
