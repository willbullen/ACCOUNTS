from django_ledger.views.bill import BillModelListView
from django_ledger.views.customer import CustomerModelListView
from django_ledger.views.vendor import VendorModelListView

class BillListShadcnView(BillModelListView):
    template_name = 'django_ledger/bills/bill_list_shadcn.html'

class CustomerListShadcnView(CustomerModelListView):
    template_name = 'django_ledger/customer/customer_list_shadcn.html'

class VendorListShadcnView(VendorModelListView):
    template_name = 'django_ledger/vendor/vendor_list_shadcn.html'
