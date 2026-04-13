from django import forms
from django.forms import inlineformset_factory
from django.utils import timezone
from .models import Product, Invoice, InvoiceItem


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_expiration_date(self):
        date = self.cleaned_data.get('expiration_date')
        if date and date < timezone.now().date():
            raise forms.ValidationError("La date de péremption ne peut pas être dans le passé.")
        return date


InvoiceItemFormSet = inlineformset_factory(
    Invoice,
    InvoiceItem,
    fields=['product', 'quantity'],
    extra=0,
    can_delete=True,
    min_num=1,
    validate_min=True,
)
