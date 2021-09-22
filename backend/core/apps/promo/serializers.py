from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from .models import Promo


class PromoSerializer(serializers.ModelSerializer):
    mobile = PhoneNumberField()

    class Meta:
        model = Promo
        fields = [
            'coupon',
            'mobile',
            'claimed_at',
            'ip_address',
            'user_agent',
        ]

    def create(self, validated_data):
        # Add ip and user agent to created object
        request = self.context.get('request')

        return Promo.objects.create(
            **validated_data,
            ip_address=self.get_ip_address(request),
            user_agent=request.META.get('HTTP_USER_AGENT')
        )

    def get_ip_address(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        return ip
