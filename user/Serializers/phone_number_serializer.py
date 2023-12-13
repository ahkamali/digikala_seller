from rest_framework import serializers
import re


class PhoneNumberSerializers(serializers.Serializer):
    phone_number = serializers.CharField(required=True)

    def validate_phone_number(self, phone_number):
        pattern = r'^0\d{10}$'
        response = bool(re.match(pattern, phone_number))
        if response:
            return response
        raise serializers.ValidationError
