# Generated by Django 3.2 on 2021-05-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
