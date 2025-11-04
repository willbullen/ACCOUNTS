from django_ledger.views.invoice import InvoiceModelListView

class InvoiceListShadcnView(InvoiceModelListView):
    template_name = 'django_ledger/invoice/invoice_list_shadcn.html'

from django_ledger.views.invoice import InvoiceModelCreateView

class InvoiceCreateShadcnView(InvoiceModelCreateView):
    template_name = 'django_ledger/invoice/invoice_create_shadcn.html'
