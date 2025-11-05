"""
Shadcn/UI CRUD Views
Custom create, update, detail views for various models with modern shadcn/ui templates.
"""

from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from django_ledger.views.mixins import DjangoLedgerSecurityMixIn
from django_ledger.views.bill import (
    BillModelCreateView,
    BillModelDetailView,
    BillModelUpdateView
)
from django_ledger.views.customer import (
    CustomerModelCreateView,
    CustomerModelUpdateView
)
from django_ledger.views.vendor import (
    VendorModelCreateView,
    VendorModelUpdateView
)
from django_ledger.views.invoice import (
    InvoiceModelListView,
    InvoiceModelCreateView,
    InvoiceModelDetailView,
    InvoiceModelUpdateView
)
from django_ledger.forms.bank_account import BankAccountCreateForm, BankAccountUpdateForm


# ============================================================================
# BILL CRUD VIEWS
# ============================================================================

class BillCreateShadcnView(BillModelCreateView):
    """Bill create view with shadcn/ui template"""
    template_name = 'django_ledger/bills/bill_create_shadcn.html'


class BillDetailShadcnView(BillModelDetailView):
    """Bill detail view with shadcn/ui template"""
    template_name = 'django_ledger/bills/bill_detail_shadcn.html'


class BillUpdateShadcnView(BillModelUpdateView):
    """Bill update view with shadcn/ui template"""
    template_name = 'django_ledger/bills/bill_update_shadcn.html'


# ============================================================================
# CUSTOMER CRUD VIEWS
# ============================================================================

class CustomerCreateShadcnView(CustomerModelCreateView):
    """Customer create view with shadcn/ui template"""
    template_name = 'django_ledger/customer/customer_create_shadcn.html'


class CustomerUpdateShadcnView(CustomerModelUpdateView):
    """Customer update view with shadcn/ui template"""
    template_name = 'django_ledger/customer/customer_update_shadcn.html'


# ============================================================================
# VENDOR CRUD VIEWS
# ============================================================================

class VendorCreateShadcnView(VendorModelCreateView):
    """Vendor create view with shadcn/ui template"""
    template_name = 'django_ledger/vendor/vendor_create_shadcn.html'


class VendorUpdateShadcnView(VendorModelUpdateView):
    """Vendor update view with shadcn/ui template"""
    template_name = 'django_ledger/vendor/vendor_update_shadcn.html'


# ============================================================================
# INVOICE CRUD VIEWS
# ============================================================================

class InvoiceListShadcnView(InvoiceModelListView):
    """Invoice list view with shadcn/ui template"""
    template_name = 'django_ledger/invoice/invoice_list_shadcn.html'


class InvoiceCreateShadcnView(InvoiceModelCreateView):
    """Invoice create view with shadcn/ui template"""
    template_name = 'django_ledger/invoice/invoice_create_shadcn.html'


class InvoiceDetailShadcnView(InvoiceModelDetailView):
    """Invoice detail view with shadcn/ui template"""
    template_name = 'django_ledger/invoice/invoice_detail_shadcn.html'


class InvoiceUpdateShadcnView(InvoiceModelUpdateView):
    """Invoice update view with shadcn/ui template"""
    template_name = 'django_ledger/invoice/invoice_update_shadcn.html'


# ============================================================================
# BANK ACCOUNT CRUD VIEWS
# ============================================================================

class BankAccountCreateShadcnView(DjangoLedgerSecurityMixIn, CreateView):
    """Bank account create view with shadcn/ui template"""
    template_name = 'django_ledger/bank_account/bank_account_create_shadcn.html'
    form_class = BankAccountCreateForm
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['entity_slug'] = self.kwargs['entity_slug']
        kwargs['user_model'] = self.request.user
        return kwargs
    
    def get_success_url(self):
        return reverse('bank-account-list-shadcn', kwargs={'entity_slug': self.kwargs['entity_slug']})


class BankAccountUpdateShadcnView(DjangoLedgerSecurityMixIn, UpdateView):
    """Bank account update view with shadcn/ui template"""
    template_name = 'django_ledger/bank_account/bank_account_update_shadcn.html'
    form_class = BankAccountUpdateForm
    pk_url_kwarg = 'bank_account_pk'
    
    def get_queryset(self):
        from django_ledger.models.bank_account import BankAccountModel
        return BankAccountModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['entity_slug'] = self.kwargs['entity_slug']
        kwargs['user_model'] = self.request.user
        return kwargs
    
    def get_success_url(self):
        return reverse('bank-account-detail-shadcn', kwargs={
            'entity_slug': self.kwargs['entity_slug'],
            'bank_account_pk': self.object.uuid
        })
