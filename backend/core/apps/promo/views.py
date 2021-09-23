from core.apps.coupon.models import Coupon
from rest_framework import views, viewsets
from rest_framework.response import Response
from twilio.base.exceptions import TwilioRestException

from .models import Promo
from .serializers import PromoSerializer, ReCaptchaSerializer


class PromoViewSet(viewsets.ModelViewSet):
    serializer_class = PromoSerializer
    queryset = Promo.objects.all()

    def create(self, request, *args, **kwargs):
        # Get IP addresss and User-Agent
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


class VerifyTokenAPI(views.APIView):
    allowed_methods = ["POST"]

    def post(self, request, *args, **kwargs):
        serializer = ReCaptchaSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'success': True}, status=200)
        return Response(serializer.errors, status=400)
