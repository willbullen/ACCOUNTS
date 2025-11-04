from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_dark_view(request):
    """Custom dark dashboard view"""
    context = {
        'page_title': 'Dashboard',
        'header_title': 'Documents',
        'header_subtitle': 'Financial overview and analytics'
    }
    return render(request, 'django_ledger/dashboard_dark.html', context)
