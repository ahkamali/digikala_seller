from django.urls import path
from product.views.change_price import ChangeProductPriceAPIView

urlpatterns = [
    path('change-price', ChangeProductPriceAPIView.as_view(), name='change-price-api'),
]