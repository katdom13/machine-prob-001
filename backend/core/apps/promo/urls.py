
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'promo'

promo_router = DefaultRouter()
promo_router.register(r'', views.PromoViewSet, basename='promo')

urlpatterns = [
    # path('', views.PromoListCreateView.as_view(), name='promo'),
    path('', include(promo_router.urls)),
]
