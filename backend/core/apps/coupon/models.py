import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Coupon(models.Model):
    """
    Model class for a coupon
    """
    public_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(
        verbose_name=_('Coupon code'),
        help_text=_('Required and unique'),
        max_length=150,
        unique=True
    )
    is_claimed = models.BooleanField(
        verbose_name=_('Is claimed'),
        help_text=_('Is this coupon claimed?'),
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
        editable=False
    )
