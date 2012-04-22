from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Crop(models.Model):
  name = models.CharField(max_length=255)
  image = models.ImageField(upload_to='crops')
  def __unicode__(self):
    return self.name

class Department(models.Model):
  name = models.CharField(max_length=255)
  image = models.ImageField(upload_to='departments')
  # TODO: Add Geo Data
  def __unicode__(self):
    return self.name

PRICE_TYPES = (
  ('local', 'Local Market'),
  ('export', 'Export Market'),
  )

class PriceReport(models.Model):
  submitter = models.ForeignKey(User, null=True)
  crop = models.ForeignKey(Crop)
  department = models.ForeignKey(Department)
  time = models.DateTimeField(auto_now_add=True)
  price_type = models.CharField(max_length=12, choices=PRICE_TYPES, default='model')
  # Amount in cents
  price = models.IntegerField()

  def __unicode__(self):
    return "%s for $%d on %s" % (self.crop, self.price, self.time)

#class Price(models.Model):
#  price_type = models.CharField(max_length=12, choices=PRICE_TYPES, default='model')
#  # Amount in cents
#  amount = models.IntegerField()
#  foreignKey = models.ForeignKey(PriceReport)
