
from django.urls import path

from . import views

app_name = 'promo'

urlpatterns = [
    path('', views.PromoListCreateView.as_view(), name='promo'),
]
