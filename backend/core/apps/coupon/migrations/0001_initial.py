# Generated by Django 3.2.7 on 2021-09-24 09:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(help_text='Required and unique', max_length=150, unique=True, verbose_name='Coupon code')),
                ('is_claimed', models.BooleanField(default=False, help_text='Is this coupon claimed?', verbose_name='Is claimed')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
        ),
    ]
