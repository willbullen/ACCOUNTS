from django_ledger.views.invoice import InvoiceModelListView

class InvoiceListShadcnView(InvoiceModelListView):
    template_name = 'django_ledger/invoice/invoice_list_shadcn.html'
