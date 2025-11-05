"""
Shadcn/UI Views Package
Modern views with shadcn/ui templates that extend Django Ledger's original functionality.
"""

# List Views
from .list_views import (
    VendorListShadcnView,
    VendorDetailShadcnView,
    CustomerListShadcnView,
    CustomerDetailShadcnView,
    BillListShadcnView,
    BankAccountListShadcnView,
    BankAccountDetailShadcnView,
)

# Financial Report Views
from .report_views import (
    BalanceSheetShadcnView,
    IncomeStatementShadcnView,
)

# Entity Views
from .entity_views import (
    entity_dashboard_shadcn,
    EntityCreateShadcnView,
)

# CRUD Views
from .crud_views import (
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

__all__ = [
    # List Views
    'VendorListShadcnView',
    'VendorDetailShadcnView',
    'CustomerListShadcnView',
    'CustomerDetailShadcnView',
    'BillListShadcnView',
    'BankAccountListShadcnView',
    'BankAccountDetailShadcnView',
    # Report Views
    'BalanceSheetShadcnView',
    'IncomeStatementShadcnView',
    # Entity Views
    'entity_dashboard_shadcn',
    'EntityCreateShadcnView',
    # CRUD Views
    'BillCreateShadcnView',
    'BillDetailShadcnView',
    'BillUpdateShadcnView',
    'CustomerCreateShadcnView',
    'CustomerUpdateShadcnView',
    'VendorCreateShadcnView',
    'VendorUpdateShadcnView',
    'InvoiceListShadcnView',
    'InvoiceCreateShadcnView',
    'InvoiceDetailShadcnView',
    'InvoiceUpdateShadcnView',
    'BankAccountCreateShadcnView',
    'BankAccountUpdateShadcnView',
]
