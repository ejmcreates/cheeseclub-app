from django import forms
from .models import Cheese, CheeseType, Review, Resource

class CheeseForm(forms.ModelForm):
    class Meta:
        model=Cheese
        fields='__all__'

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'        