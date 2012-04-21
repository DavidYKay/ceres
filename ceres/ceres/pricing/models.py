from django.db import models

# Create your models here.

class Crop(models.Model):
  name = models.CharField(max_length=255)

class Department(models.Model):
  name = models.CharField(max_length=255)
# TODO: Add 
  

class PriceReport(models.Model):
  crop = models.ForeignKey(Crop)
  department = models.ForeignKey(Department)
  time = models.DateTimeField(auto_now_add=True)
