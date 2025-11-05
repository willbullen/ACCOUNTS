"""
Shadcn/UI Entity Views
Custom entity views with modern shadcn/ui templates.
"""

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django_ledger.models import EntityModel
from django_ledger.forms.entity import EntityModelCreateForm


# ============================================================================
# ENTITY DASHBOARD VIEW
# ============================================================================

def entity_dashboard_shadcn(request, entity_slug):
    """Entity dashboard view with shadcn/ui template"""
    entity = get_object_or_404(EntityModel, slug=entity_slug)
    
    # Create minimal context with sample data
    context = {
        'entity': entity,
        'tx_digest': {
            'assets_total': 91297.75,
            'liabilities_total': 45000.00,
            'net_income': 25000.00,
            'roe_percent': 82.60,
            'roa_percent': 45.23,
            'net_profit_margin_percent': 74.76,
            'gross_profit_margin_percent': 74.76,
        },
        'equity_digest': {
            'equity_total': 46297.75,
        },
        'pnl_chart_id': 'pnl-chart',
        'pnl_chart_endpoint': '#'
    }
    
    return render(request, 'django_ledger/entity/entity_dashboard_shadcn.html', context)


# ============================================================================
# ENTITY CREATE VIEW
# ============================================================================

class EntityCreateShadcnView(LoginRequiredMixin, CreateView):
    """Entity create view with shadcn/ui template"""
    template_name = 'django_ledger/entity/entity_create_shadcn.html'
    model = EntityModel
    form_class = EntityModelCreateForm
    
    def get_success_url(self):
        return self.object.get_dashboard_url()
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
