import requests
from rest_framework import status
import json
from rest_framework.response import Response
from rest_framework.views import APIView


class VerifyOtpAPIView(APIView):
    def post(self, request):
        try:
            otp = request.data.get("otp")
            phone_number = request.data.get("phone_number")
            payload = {"otp": otp, "username": phone_number}

            verify_otp = requests.post(url='https://seller.digikala.com/api/v2/otp/verify', data=json.dumps(payload))
            if verify_otp.status_code == 201:
                data = verify_otp.json()
                access_token = data.get('data').get("token").get('access_token')
                return Response({"message": f"Your Access Token Is {access_token}"}, status=status.HTTP_200_OK)
            return Response({"message": f"OTP Is Invalid"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"message": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

