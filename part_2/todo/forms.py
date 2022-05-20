from django.forms import ModelForm
from django import forms
from .models import Item

class DateInput(forms.DateInput):
    input_type = 'date'

class addItem(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        widgets = {
            'deadline': DateInput(),
        }