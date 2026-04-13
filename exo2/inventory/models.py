from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()

    def __str__(self):
        return self.name

class Invoice(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='InvoiceItem')

    def __str__(self):
        return f"Facture n°{self.id}"

    @property
    def total_price(self):
        return sum(item.get_cost() for item in self.invoiceitem_set.all())

    @property
    def total_items(self):
        return sum(item.quantity for item in self.invoiceitem_set.all())

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.product.price * self.quantity