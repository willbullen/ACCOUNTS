from django.contrib import admin

from django_ledger.admin.coa import ChartOfAccountsModelAdmin
from django_ledger.admin.entity import EntityModelAdmin
from django_ledger.admin.ledger import LedgerModelAdmin
from django_ledger.models import (
    EntityModel, ChartOfAccountModel, LedgerModel,
    BankAccountModel, AccountModel, CustomerModel,
    UnitOfMeasureModel, ItemTransactionModel, ItemModel,
    EntityUnitModel, VendorModel, EntityStateModel,
    EntityManagementModel, BillModel, InvoiceModel,
    TransactionModel, JournalEntryModel, PurchaseOrderModel,
    EstimateModel, ClosingEntryModel, ClosingEntryTransactionModel,
    ImportJobModel, StagedTransactionModel
)

# Existing admin registrations with custom admin classes
admin.site.register(EntityModel, EntityModelAdmin)
admin.site.register(ChartOfAccountModel, ChartOfAccountsModelAdmin)
admin.site.register(LedgerModel, LedgerModelAdmin)

# Register all other models with default admin
admin.site.register(BankAccountModel)
admin.site.register(AccountModel)
admin.site.register(CustomerModel)
admin.site.register(UnitOfMeasureModel)
admin.site.register(ItemTransactionModel)
admin.site.register(ItemModel)
admin.site.register(EntityUnitModel)
admin.site.register(VendorModel)
admin.site.register(EntityStateModel)
admin.site.register(EntityManagementModel)
admin.site.register(BillModel)
admin.site.register(InvoiceModel)
admin.site.register(TransactionModel)
admin.site.register(JournalEntryModel)
admin.site.register(PurchaseOrderModel)
admin.site.register(EstimateModel)
admin.site.register(ClosingEntryModel)
admin.site.register(ClosingEntryTransactionModel)
admin.site.register(ImportJobModel)
admin.site.register(StagedTransactionModel)
