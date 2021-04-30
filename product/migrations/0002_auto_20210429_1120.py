# Generated by Django 3.2 on 2021-04-29 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('is_available', models.BooleanField(default=True)),
                ('price', models.FloatField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_items', to='product.supplier')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_items', to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='item-image/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.item')),
            ],
        ),
    ]