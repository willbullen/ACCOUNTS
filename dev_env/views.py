
from django.shortcuts import render, get_object_or_404
from django_ledger.models import EntityModel

def test_shadcn(request):
    return render(request, 'django_ledger/test_shadcn.html')

def entity_dashboard_shadcn(request, entity_slug):
    """Simplified view for shadcn dashboard"""
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
