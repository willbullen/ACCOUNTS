from django_ledger.views.invoice import InvoiceModelListView

class InvoiceListShadcnView(InvoiceModelListView):
    template_name = 'django_ledger/invoice/invoice_list_shadcn.html'

from django_ledger.views.invoice import InvoiceModelCreateView

class InvoiceCreateShadcnView(InvoiceModelCreateView):
    template_name = 'django_ledger/invoice/invoice_create_shadcn.html'

from django_ledger.views.invoice import InvoiceModelDetailView

class InvoiceDetailShadcnView(InvoiceModelDetailView):
    template_name = 'django_ledger/invoice/invoice_detail_shadcn.html'

from django_ledger.views.invoice import InvoiceModelUpdateView

class InvoiceUpdateShadcnView(InvoiceModelUpdateView):
    template_name = 'django_ledger/invoice/invoice_update_shadcn.html'
