from email.policy import default

from django.db import models

# Create your models here.
class Recipient(models.Model):
    user_location = models.CharField(max_length=30)
    user_age = models.IntegerField()
    user_gender = models.CharField(max_length=10)
    recipient_relationship = models.CharField(max_length=30)
    recipient_age = models.IntegerField()
    recipient_gender = models.CharField(max_length=30)
    recipient_interests = models.CharField(max_length=30)
    special_occasion = models.CharField(max_length=30)
    budget_preference = models.CharField(max_length=30)
    gift_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    price = models.DecimalField(default=0.0,max_digits=10, decimal_places=2)
    description = models.CharField(max_length=30)
    gift_rating = models.DecimalField(default=0.0,max_digits=10, decimal_places=2)
















