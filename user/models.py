from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


User = get_user_model()
PROFILE_CHOICES = (
    ('Card', 'Card'),
    ('Bank Account', 'Bank Account'),
    ('Paypal', 'Paypal')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    payment_method = models.CharField(max_length=30, choices=PROFILE_CHOICES, default="Card")
    number = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.full_name or "Default Full Name"

    class Meta:
        verbose_name_plural = 'Profiles'


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    Profile.objects.create(user=instance)


