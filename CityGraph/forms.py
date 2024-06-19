# citygraph/forms.py

from django import forms

class CityGraphForm(forms.Form):
    file = forms.FileField()
    origin = forms.CharField(max_length=100)
    destination = forms.CharField(max_length=100)
