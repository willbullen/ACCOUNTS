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
