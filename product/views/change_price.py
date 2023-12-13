from django.http import HttpRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import json
from product.models import ProductPricing
from datetime import datetime


class ChangeProductPriceAPIView(APIView):
    def post(self, request: HttpRequest):
        try:
            product_id = request.data.get("product_id")
            new_price = request.data.get("new_price")
            token = request.headers.get('Authorization')
            payload = {"id": int(product_id), "selling_price": int(new_price)}
            header = {'Authorization': token}
            change_product_price = requests.put(url=f'https://seller.digikala.com/api/v2/variants/{payload.get("id")}',
                                                data=json.dumps(payload), headers=header)

            if change_product_price.status_code == 200:
                ProductPricing.objects.create(product_id=product_id, price=new_price, timestamp=datetime.now())
                return Response({"message": f"The Price Of The Product With {product_id}"
                                            f" Product ID Change To {new_price} Rial."}, status=status.HTTP_200_OK)

            return Response({"message": "Invalid Request.The Product ID Or Price Entered Is Incorrect."},
                            status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"message": "Invalid Inputs."}, status=status.HTTP_400_BAD_REQUEST)
