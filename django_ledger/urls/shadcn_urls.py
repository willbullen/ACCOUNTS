"""
Shadcn/UI URL Configuration
URL patterns for all modernized views with shadcn/ui templates.
"""

from django.urls import path
from django_ledger.views.shadcn import (
    # List Views
    VendorListShadcnView,
    VendorDetailShadcnView,
    CustomerListShadcnView,
    CustomerDetailShadcnView,
    BillListShadcnView,
    BankAccountListShadcnView,
    BankAccountDetailShadcnView,
    # Report Views
    BalanceSheetShadcnView,
    IncomeStatementShadcnView,
    # Entity Views
    entity_dashboard_shadcn,
    EntityCreateShadcnView,
    # CRUD Views
    BillCreateShadcnView,
    BillDetailShadcnView,
    BillUpdateShadcnView,
    CustomerCreateShadcnView,
    CustomerUpdateShadcnView,
    VendorCreateShadcnView,
    VendorUpdateShadcnView,
    InvoiceListShadcnView,
    InvoiceCreateShadcnView,
    InvoiceDetailShadcnView,
    InvoiceUpdateShadcnView,
    BankAccountCreateShadcnView,
    BankAccountUpdateShadcnView,
)

# No app_name - URLs are at root level

urlpatterns = [
    # ============================================================================
    # ENTITY VIEWS
    # ============================================================================
    path('entity/create-shadcn/', 
         EntityCreateShadcnView.as_view(), 
         name='entity-create-shadcn'),
    
    path('entity/<slug:entity_slug>/dashboard-shadcn/', 
         entity_dashboard_shadcn, 
         name='entity-dashboard-shadcn'),
    
    # ============================================================================
    # VENDOR VIEWS
    # ============================================================================
    path('entity/<slug:entity_slug>/vendors-shadcn/', 
         VendorListShadcnView.as_view(), 
         name='vendor-list-shadcn'),
    
    path('entity/<slug:entity_slug>/vendor/create-shadcn/', 
         VendorCreateShadcnView.as_view(), 
         name='vendor-create-shadcn'),
    
    path('entity/<slug:entity_slug>/vendor/<uuid:vendor_pk>/detail-shadcn/', 
         VendorDetailShadcnView.as_view(), 
         name='vendor-detail-shadcn'),
    
    path('entity/<slug:entity_slug>/vendor/<uuid:vendor_pk>/update-shadcn/', 
         VendorUpdateShadcnView.as_view(), 
         name='vendor-update-shadcn'),
    
    # ============================================================================
    # CUSTOMER VIEWS
    # ============================================================================
    path('entity/<slug:entity_slug>/customers-shadcn/', 
         CustomerListShadcnView.as_view(), 
         name='customer-list-shadcn'),
    
    path('entity/<slug:entity_slug>/customer/create-shadcn/', 
         CustomerCreateShadcnView.as_view(), 
         name='customer-create-shadcn'),
    
    path('entity/<slug:entity_slug>/customer/<uuid:customer_pk>/detail-shadcn/', 
         CustomerDetailShadcnView.as_view(), 
         name='customer-detail-shadcn'),
    
    path('entity/<slug:entity_slug>/customer/<uuid:customer_pk>/update-shadcn/', 
         CustomerUpdateShadcnView.as_view(), 
         name='customer-update-shadcn'),
    
    # ============================================================================
    # BILL VIEWS
    # ============================================================================
    path('entity/<slug:entity_slug>/bills-shadcn/', 
         BillListShadcnView.as_view(), 
         name='bill-list-shadcn'),
    
    path('entity/<slug:entity_slug>/bill/create-shadcn/', 
         BillCreateShadcnView.as_view(), 
         name='bill-create-shadcn'),
    
    path('entity/<slug:entity_slug>/bill/<uuid:bill_pk>/detail-shadcn/', 
         BillDetailShadcnView.as_view(), 
         name='bill-detail-shadcn'),
    
    path('entity/<slug:entity_slug>/bill/<uuid:bill_pk>/update-shadcn/', 
         BillUpdateShadcnView.as_view(), 
         name='bill-update-shadcn'),
    
    # ============================================================================
    # INVOICE VIEWS
    # ============================================================================
    path('entity/<slug:entity_slug>/invoices-shadcn/', 
         InvoiceListShadcnView.as_view(), 
         name='invoice-list-shadcn'),
    
    path('entity/<slug:entity_slug>/invoice/create-shadcn/', 
         InvoiceCreateShadcnView.as_view(), 
         name='invoice-create-shadcn'),
    
    path('entity/<slug:entity_slug>/invoice/<uuid:invoice_pk>/detail-shadcn/', 
         InvoiceDetailShadcnView.as_view(), 
         name='invoice-detail-shadcn'),
    
    path('entity/<slug:entity_slug>/invoice/<uuid:invoice_pk>/update-shadcn/', 
         InvoiceUpdateShadcnView.as_view(), 
         name='invoice-update-shadcn'),
    
    # ============================================================================
    # BANK ACCOUNT VIEWS
    # ============================================================================
    path('entity/<slug:entity_slug>/bank-accounts-shadcn/', 
         BankAccountListShadcnView.as_view(), 
         name='bank-account-list-shadcn'),
    
    path('entity/<slug:entity_slug>/bank-account/create-shadcn/', 
         BankAccountCreateShadcnView.as_view(), 
         name='bank-account-create-shadcn'),
    
    path('entity/<slug:entity_slug>/bank-account/<uuid:bank_account_pk>/detail-shadcn/', 
         BankAccountDetailShadcnView.as_view(), 
         name='bank-account-detail-shadcn'),
    
    path('entity/<slug:entity_slug>/bank-account/<uuid:bank_account_pk>/update-shadcn/', 
         BankAccountUpdateShadcnView.as_view(), 
         name='bank-account-update-shadcn'),
    
    # ============================================================================
    # FINANCIAL REPORT VIEWS
    # ============================================================================
    path('entity/<slug:entity_slug>/balance-sheet-shadcn/<int:year>/', 
         BalanceSheetShadcnView.as_view(), 
         name='balance-sheet-shadcn'),
    
    path('entity/<slug:entity_slug>/income-statement-shadcn/<int:year>/', 
         IncomeStatementShadcnView.as_view(), 
         name='income-statement-shadcn'),
]
