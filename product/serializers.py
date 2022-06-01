from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):  # create class to serializer user model
    # variants = serializers.PrimaryKeyRelatedField(many=True, queryset=Variant.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'class_name', 'image', 'status')

    def to_representation(self, instance):
        data = super(ProductSerializer, self).to_representation(instance)
        data.update({"variants": instance.variants.values("title", "available_stock"),
                     "status": instance.get_status_display()})
        return data


class ProductListSerializer(serializers.ModelSerializer):  # create class to serializer user model

    class Meta:
        model = Product
        fields = ('id', 'name', 'status')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({"status": instance.get_status_display()})
        return data
