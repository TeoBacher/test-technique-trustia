from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/add/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),

    path('invoices/', views.InvoiceListView.as_view(), name='invoice-list'),
    path('invoices/create/', views.invoice_create, name='invoice-create'),
    path('invoices/<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice-detail'),
]
