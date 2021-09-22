from core.apps.coupon.models import Coupon
from rest_framework import viewsets
from rest_framework.response import Response
from twilio.base.exceptions import TwilioRestException

from .models import Promo
from .serializers import PromoSerializer


class PromoViewSet(viewsets.ModelViewSet):
    serializer_class = PromoSerializer
    queryset = Promo.objects.all()

    def create(self, request, *args, **kwargs):
        # Get IP addresss and User-Agent
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        print(request.META.get('REMOTE_ADDR'))

        try:
            code = request.data.get('code')
            mobile = request.data.get('mobile')

            coupon = Coupon.objects.filter(code=code).first()

            if not coupon:
                return Response({
                    'error': 'No coupon found'
                }, status=404)

            if coupon.is_claimed:
                return Response({
                    'error': 'Coupon already claimed'
                }, status=409)

            serializer = self.get_serializer(data={
                'coupon': coupon.public_id,
                'mobile': mobile
            })
            serializer.is_valid(raise_exception=True)

            self.perform_create(serializer)

            coupon.is_claimed = True
            coupon.save()

            return Response(serializer.data)
        except TwilioRestException:
            return Response({
                'error': 'Unable to create record: The number is unverified. Trial accounts cannot send messages to unverified numbers; verify at twilio.com/user/account/phone-numbers/verified, or purchase a Twilio number to send messages to unverified numbers.'
            }, status=400)
