import locale

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
locale.setlocale( locale.LC_ALL, '' )

class Crop(models.Model):
  name = models.CharField(max_length=255)
  image = models.ImageField(upload_to='crops', blank=True)
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

#UNIT_TYPES = (
#  ('quintal', 'quintal'),
#  ('kg', 'kg'),
#  ('lb', 'lb'),
#  ('bushel', 'bushel'),
#  )

class Currency(models.Model):
  name = models.CharField(max_length=127)
  symbol = models.CharField(max_length=4)
  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name_plural = "currencies"

class WeightUnit(models.Model):
  name = models.CharField(max_length=127)
  symbol = models.CharField(max_length=8)

  def __unicode__(self):
    return self.name

class PriceReport(models.Model):
  submitter = models.ForeignKey(User, null=True)
  crop = models.ForeignKey(Crop)
  department = models.ForeignKey(Department)
  time = models.DateTimeField(auto_now_add=True)
  # Amount in cents
  price = models.IntegerField()
  price_type = models.CharField(max_length=12, choices=PRICE_TYPES,
                                default='local')
  weight_unit = models.ForeignKey(WeightUnit)
  currency = models.ForeignKey(Currency)

  def formatted_price(self):
    #return locale.currency(float(self.price) / float(100), grouping=True )
    return "%s%d" % (currency, price)

  def department_first(self):
    return "%s, %s, %s" % (self.department, self.crop, self.formatted_price())

  def crop_first(self):
    return "%s, %s" % (self.crop, self.formatted_price())

  def __unicode__(self):
    #return "%s for $%d on %s" % (self.crop, self.price, self.time)
    #return "%s for $%d in %s" % (self.crop, self.price, self.time)
    #return "%s : $%d : %s" % (self.crop, self.price, self.department)
    return self.department_first()

#class Price(models.Model):
#  price_type = models.CharField(max_length=12, choices=PRICE_TYPES, default='model')
#  # Amount in cents
#  amount = models.IntegerField()
#  foreignKey = models.ForeignKey(PriceReport)
