from django.contrib import admin
from models import Crop, Department, PriceReport


class CropAdmin(admin.ModelAdmin):
  pass

admin.site.register(Crop, CropAdmin)

class DepartmentAdmin(admin.ModelAdmin):
  pass
admin.site.register(Department, DepartmentAdmin)

class PriceReportAdmin(admin.ModelAdmin):
  list_filter = ('crop', 'department', 'price_type', 'time')
admin.site.register(PriceReport, PriceReportAdmin)
