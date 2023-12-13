from django.urls import path
from user.auth_views.request_otp import RequestOtpAPIView
from user.auth_views.verify_otp import VerifyOtpAPIView

urlpatterns = [
    path('request-otp', RequestOtpAPIView.as_view(), name='request-otp-api'),
    path('verify-otp', VerifyOtpAPIView.as_view(), name='verify-otp-api'),
]