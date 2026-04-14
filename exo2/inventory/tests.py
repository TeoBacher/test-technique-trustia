from datetime import date, timedelta
from django.test import TestCase
from django.urls import reverse
from .models import Product, Invoice, InvoiceItem
from .forms import ProductForm, InvoiceItemForm


# Models

class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Pomme',
            price=1.50,
            expiration_date=date.today() + timedelta(days=10),
        )

    def test_str(self):
        self.assertEqual(str(self.product), 'Pomme')


class InvoiceModelTest(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create(
            name='Pomme',
            price=2.00,
            expiration_date=date.today() + timedelta(days=10),
        )
        self.product2 = Product.objects.create(
            name='Banane',
            price=1.50,
            expiration_date=date.today() + timedelta(days=5),
        )
        self.invoice = Invoice.objects.create()
        InvoiceItem.objects.create(invoice=self.invoice, product=self.product1, quantity=3)
        InvoiceItem.objects.create(invoice=self.invoice, product=self.product2, quantity=2)

    def test_total_price(self):
        self.assertEqual(self.invoice.total_price, 9.00)

    def test_total_items(self):
        self.assertEqual(self.invoice.total_items, 5)

    def test_str(self):
        self.assertEqual(str(self.invoice), f"Facture n°{self.invoice.id}")


class InvoiceItemModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Pomme',
            price=2.00,
            expiration_date=date.today() + timedelta(days=10),
        )
        self.invoice = Invoice.objects.create()
        self.item = InvoiceItem.objects.create(
            invoice=self.invoice,
            product=self.product,
            quantity=4,
        )

    def test_get_cost(self):
        self.assertEqual(self.item.get_cost(), 8.00)


# Forms

class ProductFormTest(TestCase):

    def test_valid_form(self):
        form = ProductForm(data={
            'name': 'Pomme',
            'price': 1.50,
            'expiration_date': date.today() + timedelta(days=10),
        })
        self.assertTrue(form.is_valid())

    def test_past_expiration_date(self):
        form = ProductForm(data={
            'name': 'Pomme',
            'price': 1.50,
            'expiration_date': date.today() - timedelta(days=1),
        })
        self.assertFalse(form.is_valid())
        self.assertIn('expiration_date', form.errors)

    def test_price_zero(self):
        form = ProductForm(data={
            'name': 'Pomme',
            'price': 0,
            'expiration_date': date.today() + timedelta(days=10),
        })
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors)

    def test_price_negative(self):
        form = ProductForm(data={
            'name': 'Pomme',
            'price': -5,
            'expiration_date': date.today() + timedelta(days=10),
        })
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors)


class InvoiceItemFormTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Pomme',
            price=1.50,
            expiration_date=date.today() + timedelta(days=10),
        )

    def test_quantity_zero(self):
        form = InvoiceItemForm(data={
            'product': self.product.id,
            'quantity': 0,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors)


# Views 

class ProductViewTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Pomme',
            price=1.50,
            expiration_date=date.today() + timedelta(days=10),
        )

    def test_product_list(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pomme')

    def test_product_create(self):
        response = self.client.post(reverse('product-create'), {
            'name': 'Banane',
            'price': 0.99,
            'expiration_date': date.today() + timedelta(days=5),
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.filter(name='Banane').exists())

    def test_product_update(self):
        response = self.client.post(reverse('product-update', args=[self.product.pk]), {
            'name': 'Pomme modifiée',
            'price': 2.00,
            'expiration_date': date.today() + timedelta(days=10),
        })
        self.assertEqual(response.status_code, 302)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Pomme modifiée')

    def test_product_delete(self):
        response = self.client.post(reverse('product-delete', args=[self.product.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())


class InvoiceViewTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Pomme',
            price=1.50,
            expiration_date=date.today() + timedelta(days=10),
        )
        self.invoice = Invoice.objects.create()
        InvoiceItem.objects.create(invoice=self.invoice, product=self.product, quantity=2)

    def test_invoice_list(self):
        response = self.client.get(reverse('invoice-list'))
        self.assertEqual(response.status_code, 200)

    def test_invoice_detail(self):
        response = self.client.get(reverse('invoice-detail', args=[self.invoice.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pomme')
