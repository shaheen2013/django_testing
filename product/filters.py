from django_filters import rest_framework as filters
from .models import Product


# We create filters for each field we want to be able to filter on
class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    klass = filters.CharFilter(lookup_expr='icontains')
    status = filters.CharFilter(method='status_filter')

    def status_filter(self, queryset, name, value):
        if value == "available":
            value = 1
        elif value == "unavailable":
            value = 2
        else:
            value = 0
        return queryset.filter(status=value)

    class Meta:
        model = Product
        fields = ['name', 'klass', 'status']

