from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.response import Response

from .models import Product, Variant
from .serializers import ProductSerializer, ProductListSerializer
from .filters import ProductFilter


class ProductDetailsAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # permission_classes = [IsAuthenticated]


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"success": True})

    def perform_create(self, serializer):
        product = serializer.save()
        variants = list(self.request.data.get("variants"))
        for variant in variants:
            variant = dict(variant)
            variant.update({"product_id": product.id})
            Variant.objects.create(**variant)


class UpdateProductAPIView(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"success": True })

    def perform_update(self, serializer):
        product = serializer.save()
        product.variants.all().delete()
        variants = list(self.request.data.get("variants"))
        for variant in variants:
            variant = dict(variant)
            variant.update({"product_id": product.id})
            Variant.objects.create(**variant)


class DeleteProductAPIView(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"success": True})


class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    # permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {'data': response.data}
        return response


