from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.CASCADE,
                               related_name='children',
                               limit_choices_to={'is_child': False})
    is_child = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Supplier(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_items")
    brand = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="supplier_items")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    price = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to="item-image/")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="images")