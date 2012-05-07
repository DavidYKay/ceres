from django.contrib import admin
from models import *


class CropAdmin(admin.ModelAdmin):
  pass
admin.site.register(Crop, CropAdmin)

class DepartmentAdmin(admin.ModelAdmin):
  pass
admin.site.register(Department, DepartmentAdmin)

class PriceReportAdmin(admin.ModelAdmin):
  list_display = ( 'department', 'crop', 'price', 'currency' )
  list_filter = ('crop', 'department', 'price_type', 'time')
admin.site.register(PriceReport, PriceReportAdmin)

class CurrencyAdmin(admin.ModelAdmin):
  list_display = ( 'symbol', 'name', )
admin.site.register(Currency, CurrencyAdmin)

class WeightUnitAdmin(admin.ModelAdmin):
  list_display = ( 'name', 'symbol', )
admin.site.register(WeightUnit, WeightUnitAdmin)
