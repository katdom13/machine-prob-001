from core.apps.coupon.models import Coupon
from django.db import models
from django.utils.translation import gettext_lazy as _


class Promo(models.Model):
    """
    Model class for a promo
    """
    coupon = models.OneToOneField(
        Coupon,
        verbose_name=_('Coupon'),
        on_delete=models.CASCADE
    )
    mobile = models.CharField(
        verbose_name=_('Mobile number'),
        max_length=15
    )
    claimed_at = models.DateTimeField(
        verbose_name=_('Claimed at'),
        auto_now_add=True,
        editable=False
    )
