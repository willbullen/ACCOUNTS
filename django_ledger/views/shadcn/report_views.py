"""
Shadcn/UI Financial Report Views
Custom financial statement views that extend Django Ledger's original views with modern shadcn/ui templates.
"""

from django.urls import reverse
from django_ledger.views.financial_statement import (
    FiscalYearBalanceSheetView,
    FiscalYearIncomeStatementView
)


# ============================================================================
# BALANCE SHEET VIEW
# ============================================================================

class BalanceSheetShadcnView(FiscalYearBalanceSheetView):
    """Balance Sheet view with shadcn/ui template"""
    template_name = 'django_ledger/financial_statements/balance_sheet_shadcn.html'
    
    def get_context_data(self, **kwargs):
        """Override to add balance sheet digest data to context"""
        context = super().get_context_data(**kwargs)
        
        # Get the entity model (io_model)
        io_model = self.object
        
        # Get parameters from request
        activity = self.request.GET.get('activity')
        to_date = context.get('to_date')
        unit_slug = context.get('unit_slug')
        by_unit = context.get('by_unit')
        
        # Generate the balance sheet digest
        io_digest = io_model.digest(
            activity=activity,
            user_model=self.request.user,
            equity_only=False,
            entity_slug=self.kwargs.get('entity_slug'),
            unit_slug=unit_slug,
            by_unit=by_unit,
            to_date=to_date,
            signs=True,
            process_groups=True,
            balance_sheet_statement=True
        )
        
        # Add the digest data to context
        context['tx_digest'] = io_digest.get_io_data()
        
        return context
    
    def get_base_date_nav_url(self, context, **kwargs):
        """Override to use our custom URL name for date navigation"""
        # Include entity_slug and year for the balance sheet URL
        url_kwargs = {'entity_slug': self.kwargs['entity_slug']}
        if 'year' in self.kwargs:
            url_kwargs['year'] = self.kwargs['year']
        context['date_navigation_url'] = reverse('balance-sheet-shadcn', kwargs=url_kwargs)


# ============================================================================
# INCOME STATEMENT VIEW
# ============================================================================

class IncomeStatementShadcnView(FiscalYearIncomeStatementView):
    """Income Statement view with shadcn/ui template"""
    template_name = 'django_ledger/financial_statements/income_statement_shadcn.html'
    
    def get_context_data(self, **kwargs):
        """Override to add income statement digest data to context"""
        context = super().get_context_data(**kwargs)
        
        # Get the entity model (io_model)
        io_model = self.object
        
        # Get parameters from request
        activity = self.request.GET.get('activity')
        from_date = context.get('from_date')
        to_date = context.get('to_date')
        unit_slug = context.get('unit_slug')
        by_unit = context.get('by_unit')
        
        # Generate the income statement digest
        io_digest = io_model.digest(
            activity=activity,
            user_model=self.request.user,
            entity_slug=self.kwargs.get('entity_slug'),
            unit_slug=unit_slug,
            by_unit=by_unit,
            from_date=from_date,
            to_date=to_date,
            equity_only=True,
            process_groups=True,
            income_statement=True,
            signs=True
        )
        
        # Add the digest data to context
        context['tx_digest'] = io_digest.get_io_data()
        
        return context
    
    def get_base_date_nav_url(self, context, **kwargs):
        """Override to use our custom URL name for date navigation"""
        # Include entity_slug and year for the income statement URL
        url_kwargs = {'entity_slug': self.kwargs['entity_slug']}
        if 'year' in self.kwargs:
            url_kwargs['year'] = self.kwargs['year']
        context['date_navigation_url'] = reverse('income-statement-shadcn', kwargs=url_kwargs)
