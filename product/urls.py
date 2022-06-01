from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/details/', views.ProductDetailsAPIView.as_view(), name='product_details'),
    path('create/', views.ProductCreateAPIView.as_view(), name='product_create'),
    path('<int:pk>/update/', views.UpdateProductAPIView.as_view(), name='product_update'),
    path('<int:pk>/delete/', views.DeleteProductAPIView.as_view(), name='delete_product'),
    path('list/', views.ProductListAPIView.as_view(), name='product_list'),
]