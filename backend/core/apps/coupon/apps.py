from django.apps import AppConfig


class CouponConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.apps.coupon'

    def ready(self):
        import core.apps.coupon.signals
