# Generated by Django 3.2.7 on 2021-09-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0002_alter_promo_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='promo',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, verbose_name='IP Address'),
        ),
        migrations.AddField(
            model_name='promo',
            name='user_agent',
            field=models.CharField(blank=True, max_length=150, verbose_name='User Agent'),
        ),
    ]
