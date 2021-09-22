from core.apps.coupon.models import Coupon
from core.twilio import twilio_client
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Promo(models.Model):
    """
    Model class for a promo
    """
    coupon = models.OneToOneField(
        Coupon,
        verbose_name=_('Coupon'),
        on_delete=models.CASCADE
    )
    mobile = PhoneNumberField()
    claimed_at = models.DateTimeField(
        verbose_name=_('Claimed at'),
        auto_now_add=True,
        editable=False
    )
    ip_address = models.GenericIPAddressField(verbose_name=_('IP Address'), null=True)
    user_agent = models.CharField(
        verbose_name=_('User Agent'),
        max_length=150,
        blank=True
    )

    def save(self, *args, **kwargs):
        # message = twilio_client.messages.create(
        #     body=f'You have successfully won a prize using coupon code: {self.coupon.code}. Please contact us to receive instructions to claim the prize.',
        #     from_=settings.TWILIO_PHONE_NUMBER,
        #     to=str(self.mobile)
        # )

        # print('==============MESSAGE SID===============')
        # print(message.sid)

        return super().save(*args, **kwargs)
