from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate, login

from models import PriceReport

class PriceReportForm(ModelForm):
  class Meta:
    model = PriceReport
    #fields = ( 'username', 'password', 'first_name', 'last_name', 'streetAddress', 'zipCode', 'phoneNumber',)
    #exclude = ('is_staff', 'is_active', 'date_joined', 'last_login')
