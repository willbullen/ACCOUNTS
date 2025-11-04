from django_ledger.views.bill import BillModelListView
from django_ledger.views.customer import CustomerModelListView
from django_ledger.views.vendor import VendorModelListView

class BillListShadcnView(BillModelListView):
    template_name = 'django_ledger/bills/bill_list_shadcn.html'

class CustomerListShadcnView(CustomerModelListView):
    template_name = 'django_ledger/customer/customer_list_shadcn.html'

class VendorListShadcnView(VendorModelListView):
    template_name = 'django_ledger/vendor/vendor_list_shadcn.html'

from django_ledger.views.bill import BillModelCreateView

class BillCreateShadcnView(BillModelCreateView):
    template_name = 'django_ledger/bills/bill_create_shadcn.html'

from django_ledger.views.customer import CustomerModelCreateView

class CustomerCreateShadcnView(CustomerModelCreateView):
    template_name = 'django_ledger/customer/customer_create_shadcn.html'

from django_ledger.views.vendor import VendorModelCreateView

class VendorCreateShadcnView(VendorModelCreateView):
    template_name = 'django_ledger/vendor/vendor_create_shadcn.html'
from django_ledger.views.bill import BillModelDetailView

class BillDetailShadcnView(BillModelDetailView):
    template_name = 'django_ledger/bills/bill_detail_shadcn.html'

from django_ledger.views.bill import BillModelUpdateView

class BillUpdateShadcnView(BillModelUpdateView):
    template_name = 'django_ledger/bills/bill_update_shadcn.html'

from django_ledger.views.customer import CustomerModelUpdateView

class CustomerUpdateShadcnView(CustomerModelUpdateView):
    template_name = 'django_ledger/customer/customer_update_shadcn.html'

from django_ledger.views.vendor import VendorModelUpdateView

class VendorUpdateShadcnView(VendorModelUpdateView):
    template_name = 'django_ledger/vendor/vendor_update_shadcn.html'

from django.views.generic import DetailView
from django_ledger.models.customer import CustomerModel
from django_ledger.models.vendor import VendorModel

class CustomerDetailShadcnView(DetailView):
    model = CustomerModel
    template_name = 'django_ledger/customer/customer_detail_shadcn.html'
    context_object_name = 'customer'
    pk_url_kwarg = 'customer_pk'
    
    def get_queryset(self):
        return CustomerModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

class VendorDetailShadcnView(DetailView):
    model = VendorModel
    template_name = 'django_ledger/vendor/vendor_detail_shadcn.html'
    context_object_name = 'vendor'
    pk_url_kwarg = 'vendor_pk'
    
    def get_queryset(self):
        return VendorModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

# Bank Account Views
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django_ledger.views.mixins import DjangoLedgerSecurityMixIn
from django_ledger.forms.bank_account import BankAccountCreateForm, BankAccountUpdateForm
from django.urls import reverse

class BankAccountListShadcnView(DjangoLedgerSecurityMixIn, ListView):
    template_name = 'django_ledger/bank_account/bank_account_list_shadcn.html'
    context_object_name = 'bank_accounts'
    
    def get_queryset(self):
        from django_ledger.models.bank_account import BankAccountModel
        return BankAccountModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('cash_account', 'entity_model')


class BankAccountDetailShadcnView(DjangoLedgerSecurityMixIn, DetailView):
    template_name = 'django_ledger/bank_account/bank_account_detail_shadcn.html'
    context_object_name = 'object'
    pk_url_kwarg = 'bank_account_pk'
    
    def get_queryset(self):
        from django_ledger.models.bank_account import BankAccountModel
        return BankAccountModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('cash_account', 'entity_model')


class BankAccountCreateShadcnView(DjangoLedgerSecurityMixIn, CreateView):
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
