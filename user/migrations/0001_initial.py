# Generated by Django 3.2 on 2021-04-30 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('full_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('payment_method', models.CharField(choices=[('Card', 'Card'), ('Bank Account', 'Bank Account'), ('Paypal', 'Paypal')], max_length=30)),
                ('number', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]