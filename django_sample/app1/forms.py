from django import forms
from .models import TestData


class TestDataModelForm(forms.ModelForm):

    class Meta:
        model = TestData
        fields = ("number", "name", "price")
