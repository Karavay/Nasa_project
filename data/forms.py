from django import forms
from django.core import validators
from .models import Apod

class DataForm(forms.Form):
    year = forms.IntegerField(label='year',max_value=2020,min_value=1995)
    month = forms.IntegerField(label='month',max_value=12,min_value=1)
    day = forms.IntegerField(label='day',min_value=1,max_value=31)

class DataInTimeForm(forms.Form):
    amount_of_time = forms.IntegerField(label='time')
    year = forms.IntegerField(label='year',max_value=2020,min_value=1995)
    month = forms.IntegerField(label='month',max_value=12,min_value=1)
    day = forms.IntegerField(label='day',min_value=1,max_value=31)
