from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.db import transaction

from .models import Product, Invoice
from .forms import ProductForm, InvoiceItemFormSet


class ProductListView(ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    ordering = ['name']


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product-list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product-list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')


#  Factures

class InvoiceListView(ListView):
    model = Invoice
    template_name = 'inventory/invoice_list.html'
    context_object_name = 'invoices'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        return super().get_queryset().prefetch_related('invoiceitem_set__product')


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'inventory/invoice_detail.html'
    context_object_name = 'invoice'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('invoiceitem_set__product')


def invoice_create(request):
    invoice = Invoice()
    if request.method == 'POST':
        formset = InvoiceItemFormSet(request.POST, instance=invoice)
        if formset.is_valid():
            with transaction.atomic():
                invoice.save()
                formset.save()
            return redirect('invoice-detail', pk=invoice.pk)
    else:
        formset = InvoiceItemFormSet(instance=invoice)
    return render(request, 'inventory/invoice_create.html', {'formset': formset})
