from django import forms
from django.forms import inlineformset_factory
from .models import Product, Invoice, InvoiceItem


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }


InvoiceItemFormSet = inlineformset_factory(
    Invoice,
    InvoiceItem,
    fields=['product', 'quantity'],
    extra=0,
    can_delete=True,
    min_num=1,
    validate_min=True,
)
