from django import forms
from django.forms import ModelForm

from .models import *
#from project.project import settings
#from project.pro.models import Discount, Seat, Schedule

'''
class Book(forms.Form):
    seat = forms.ModelChoiceField(queryset=Seat.objects.all())
    user = forms.CharField(max_length=400, label='username')
    discount = forms.ModelChoiceField(queryset=Discount.objects.all())
    price_dis = forms.FloatField()
    shed_id = forms.ModelChoiceField(queryset=Schedule.objects.all())
    total_price = forms.FloatField()
'''
class Book(ModelForm):
    class Meta:
        model = Reservation
        fields = ['seat', 'user','shed_id','discount','type', 'payment']#'__all__'

