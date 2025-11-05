"""
Shadcn/UI List Views
Custom list views that extend Django Ledger's original views with modern shadcn/ui templates.
"""

from django.views.generic import ListView, DetailView
from django_ledger.views.mixins import DjangoLedgerSecurityMixIn
from django_ledger.views.bill import BillModelListView
from django_ledger.views.customer import CustomerModelListView
from django_ledger.views.vendor import VendorModelListView
from django_ledger.models.customer import CustomerModel
from django_ledger.models.vendor import VendorModel


# ============================================================================
# VENDOR VIEWS
# ============================================================================

class VendorListShadcnView(VendorModelListView):
    """Vendor list view with shadcn/ui template"""
    template_name = 'django_ledger/vendor/vendor_list_shadcn.html'


class VendorDetailShadcnView(DetailView):
    """Vendor detail view with shadcn/ui template"""
    model = VendorModel
    template_name = 'django_ledger/vendor/vendor_detail_shadcn.html'
    context_object_name = 'vendor'
    pk_url_kwarg = 'vendor_pk'
    
    def get_queryset(self):
        return VendorModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )


# ============================================================================
# CUSTOMER VIEWS
# ============================================================================

class CustomerListShadcnView(CustomerModelListView):
    """Customer list view with shadcn/ui template"""
    template_name = 'django_ledger/customer/customer_list_shadcn.html'


class CustomerDetailShadcnView(DetailView):
    """Customer detail view with shadcn/ui template"""
    model = CustomerModel
    template_name = 'django_ledger/customer/customer_detail_shadcn.html'
    context_object_name = 'customer'
    pk_url_kwarg = 'customer_pk'
    
    def get_queryset(self):
        return CustomerModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )


# ============================================================================
# BILL VIEWS
# ============================================================================

class BillListShadcnView(BillModelListView):
    """Bill list view with shadcn/ui template"""
    template_name = 'django_ledger/bills/bill_list_shadcn.html'


# ============================================================================
# BANK ACCOUNT VIEWS
# ============================================================================

class BankAccountListShadcnView(DjangoLedgerSecurityMixIn, ListView):
    """Bank account list view with shadcn/ui template"""
    template_name = 'django_ledger/bank_account/bank_account_list_shadcn.html'
    context_object_name = 'bank_accounts'
    
    def get_queryset(self):
        from django_ledger.models.bank_account import BankAccountModel
        return BankAccountModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('cash_account', 'entity_model')


class BankAccountDetailShadcnView(DjangoLedgerSecurityMixIn, DetailView):
    """Bank account detail view with shadcn/ui template"""
    template_name = 'django_ledger/bank_account/bank_account_detail_shadcn.html'
    context_object_name = 'object'
    pk_url_kwarg = 'bank_account_pk'
    
    def get_queryset(self):
        from django_ledger.models.bank_account import BankAccountModel
        return BankAccountModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('cash_account', 'entity_model')
