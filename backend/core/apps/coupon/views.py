import os

from core.apps.coupon.models import Coupon
from django.conf import settings
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .storage import OverwriteStorage


class UploadCouponList(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        rewrite = request.GET.get('rewrite')
        is_rewrite = False
        file = request.FILES.get('file')

        fs = OverwriteStorage()
        fs.save(file.name, file)

        saved_file = os.path.join(settings.MEDIA_ROOT, file.name)

        with open(saved_file, 'r') as sfile:
            codes = sfile.read().splitlines()

        if rewrite:
            is_rewrite = True if rewrite.lower() in ['true', '1'] else False

        if is_rewrite:
            Coupon.objects.all().delete()

        for code in codes:
            hashed_code = Coupon.hash_code(code)
            coupon = Coupon.objects.filter(code=hashed_code).first()
            if not coupon:
                Coupon.objects.create(code=code)

        return Response({
            'success': 'All coupons uploaded to the database.'
        }, status=200)
