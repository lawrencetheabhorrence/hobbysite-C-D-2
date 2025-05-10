from django import forms
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from .models import Transaction, Product, ProductType
from user_management.models import Profile
"""
					{% for error in form.non_field_errors %}
						{{ error|escape }}
					{% endfor %}
"""


class ProductCreator(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        self.owner_profile = kwargs.pop('owner', None)
        super().__init__(*args, **kwargs)
        self.fields['owner'].widget = forms.HiddenInput(attrs={"readonly": "true" })
        '''self.fields['owner'].choices = [self.owner_profile]
        print(self.fields['owner'].choices)'''
        self.initial['owner'] = self.owner_profile

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {"stock": forms.NumberInput(attrs={"min": "1"})}