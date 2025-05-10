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
    def __init__(self,user,*args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        self.fields['owner'].widget = forms.TextInput(attrs={"readonly": "true" })
        self.fields['owner'].choices = [user.profile.name]
        print(self.fields['owner'].choices)
        self.initial['owner'] = user.profile.name

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {"stock": forms.NumberInput(attrs={"min": "1"})}