from django_filters import rest_framework as filters
from .models import Product


# We create filters for each field we want to be able to filter on
class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    klass = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'klass', 'status']

