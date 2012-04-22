from django.db import models
from django.contrib.auth import User

# Create your models here.

class Crop(models.Model):
  name = models.CharField(max_length=255)

class Department(models.Model):
  name = models.CharField(max_length=255)
  # TODO: Add Geo Data

PRICE_TYPES = (
  ('local', '3D Model'),
  ('export', 'Texture'),
  )

class PriceReport(models.Model):
  submitter = models.ForeignKey(User)
  crop = models.ForeignKey(Crop)
  department = models.ForeignKey(Department)
  time = models.DateTimeField(auto_now_add=True)
  price_type = models.CharField(max_length=12, choices=PRICE_TYPES, default='model')
  # Amount in cents
  price = models.IntegerField()

#class Price(models.Model):
#  price_type = models.CharField(max_length=12, choices=PRICE_TYPES, default='model')
#  # Amount in cents
#  amount = models.IntegerField()
#  foreignKey = models.ForeignKey(PriceReport)
