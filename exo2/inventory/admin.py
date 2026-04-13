from django.contrib import admin
from .models import Product, Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]
    list_display = ('id', 'created_at', 'get_total_display')

    def get_total_display(self, obj):
        return f"{obj.total_price} €"
    
    get_total_display.short_description = 'Total à payer'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'expiration_date')