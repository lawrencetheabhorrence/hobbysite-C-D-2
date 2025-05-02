from django import forms
from django.shortcuts import get_object_or_404
from django.forms import ModelChoiceField
#from django.core.exceptions import ValidationError
from .models import Transaction, Product, Profile

class TransactionForm(forms.ModelForm):
    product = None
    
    def __init__(self, *args,  item=None, **kwargs,):
        super().__init__(*args, **kwargs)
        self.product = item
        
    class Meta:
        model = Transaction
        fields = ['amount']
        
    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get('amount')
        
        if amount!=None and self.product!=None:
            if self.product.stock < amount:
                self.add_error('amount',"Buying too much")
            if amount<=0:
                self.add_error('amount',"You are buying nothing")
        return cleaned_data
'''
					{% for error in form.non_field_errors %}
						{{ error|escape }}
					{% endfor %}
'''

class ProductCreator(forms.ModelForm):
    owner = ModelChoiceField(disabled=True, queryset=Profile.objects.all())
    class Meta:
        model = Product
        fields = '__all__'
