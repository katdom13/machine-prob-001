from core.apps.coupon.models import Coupon
from django.http import response
from rest_framework import generics
from rest_framework.response import Response

from .models import Promo
from .serializers import PromoSerializer


class PromoListCreateView(generics.ListCreateAPIView):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer

    def create(self, request, *args, **kwargs):
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

        promo = Promo.objects.create(
            coupon=coupon,
            mobile=mobile
        )

        coupon.is_claimed = True
        coupon.save()

        serializer = self.get_serializer(promo, many=False)

        return Response(serializer.data)
