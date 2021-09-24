from core.utils import hash_string
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Coupon


@receiver(post_save, sender=Coupon)
def hash_coupon_code(sender, instance, created, **kwargs):
    # Hash coupon code upon creation
    if created:
        instance.code = hash_string(instance.code)
        instance.save()
