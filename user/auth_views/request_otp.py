import requests
from django.http import HttpRequest
from rest_framework import status
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from user.Serializers.phone_number_serializer import PhoneNumberSerializers


class RequestOtpAPIView(APIView):
    def post(self, request: HttpRequest):
        try:
            phone_number = request.data.get("phone_number")
            serialized = PhoneNumberSerializers(data=request.data)

            if serialized.is_valid():
                payload = {"username": phone_number}

                data = requests.post(url='https://seller.digikala.com/api/v2/otp/send', data=json.dumps(payload))
                if data.status_code == 200:
                    return Response({"message": f"We Send A Code To {phone_number}"}, status=status.HTTP_200_OK)
            return Response({"message": "Phone Number Is Incorrect Or Is Invalid."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

