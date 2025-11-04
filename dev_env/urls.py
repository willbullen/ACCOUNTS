from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from dev_env import views
from dev_env.views_invoice import InvoiceListShadcnView
from dev_env.views_lists import BillListShadcnView, CustomerListShadcnView, VendorListShadcnView
from dev_env.views_entity import EntityCreateShadcnView

from django_ledger.settings import DJANGO_LEDGER_GRAPHQL_SUPPORT_ENABLED
from django_ledger.views_custom import dashboard_dark_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test-shadcn/', views.test_shadcn, name='test-shadcn'),
    path('entity/<slug:entity_slug>/dashboard-shadcn/', views.entity_dashboard_shadcn, name='entity-dashboard-shadcn'),
    path('entity/<slug:entity_slug>/invoices-shadcn/', InvoiceListShadcnView.as_view(), name='invoice-list-shadcn'),
    path('entity/<slug:entity_slug>/bills-shadcn/', BillListShadcnView.as_view(), name='bill-list-shadcn'),
    path('entity/<slug:entity_slug>/customers-shadcn/', CustomerListShadcnView.as_view(), name='customer-list-shadcn'),
    path('entity/<slug:entity_slug>/vendors-shadcn/', VendorListShadcnView.as_view(), name='vendor-list-shadcn'),
    path('entity/create-shadcn/', EntityCreateShadcnView.as_view(), name='entity-create-shadcn'),
    path('dashboard/', dashboard_dark_view, name='dashboard_dark'),
    path('', include('django_ledger.urls', namespace='django_ledger')),
]

# GraphQl API Support...
try:
    if DJANGO_LEDGER_GRAPHQL_SUPPORT_ENABLED:
        from django_ledger.contrib.django_ledger_graphene.api import schema
        from django_ledger.contrib.django_ledger_graphene.views import DjangoLedgerOAuth2GraphQLView

        urlpatterns += [
            path('api/v1/graphql/', DjangoLedgerOAuth2GraphQLView.as_view(graphiql=settings.DEBUG, schema=schema)),
            path('api/v1/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
        ]

except ImportError:
    pass
