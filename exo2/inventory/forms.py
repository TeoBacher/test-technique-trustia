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

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Le prix doit être supérieur à 0.")
        return price


class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['product', 'quantity']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is not None and quantity < 1:
            raise forms.ValidationError("La quantité doit être au moins 1.")
        return quantity


InvoiceItemFormSet = inlineformset_factory(
    Invoice,
    InvoiceItem,
    form=InvoiceItemForm,
    extra=0,
    can_delete=True,
    min_num=1,
    validate_min=True,
)
