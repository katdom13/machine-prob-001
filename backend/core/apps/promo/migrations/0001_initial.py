# Generated by Django 3.2.7 on 2021-09-22 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=15, verbose_name='Mobile number')),
                ('claimed_at', models.DateTimeField(auto_now_add=True, verbose_name='Claimed at')),
                ('coupon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='coupon.coupon', verbose_name='Coupon')),
            ],
        ),
    ]
