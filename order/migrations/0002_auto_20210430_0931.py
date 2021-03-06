# Generated by Django 3.2 on 2021-04-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(blank=True, choices=[('Door delivery', 'Door delivery'), ('Pick up', 'Pick up')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('Card', 'Card'), ('Bank Account', 'Bank Account'), ('Paypal', 'Paypal')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
