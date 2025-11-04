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
