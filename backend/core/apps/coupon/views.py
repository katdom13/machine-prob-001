from core.apps.coupon.models import Coupon
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView


class UploadCouponList(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        rewrite = request.GET.get('rewrite')
        is_rewrite = False
        file = request.FILES.get('file')
        codes = [line.decode('utf-8').strip() for line in file.readlines()]
        response = {
            'success': 'All coupons uploaded to the database.'
        }

        if rewrite:
            is_rewrite = True if rewrite.lower() in ['true', '1'] else False

        if is_rewrite:
            Coupon.objects.all().delete()

        for code in codes:
            hashed_code = Coupon.hash_code(code)
            coupon = Coupon.objects.filter(code=hashed_code).first()
            if not coupon:
                Coupon.objects.create(code=code)

        return Response(response, status=200)
