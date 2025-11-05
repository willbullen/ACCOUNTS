# Code Location Guide: Where Everything Lives

## Your Question

> "So is all the code in dev_env?"

## The Answer

**No, the code is split between two locations:**

1. **`dev_env/`** - Custom views and URL routing (Python code)
2. **`django_ledger/templates/`** - Custom templates (HTML/CSS)

Let me explain why and show you exactly where everything is.

## Directory Structure

```
django-accounting-system/
├── dev_env/                          ← Custom Python code (views, URLs, settings)
│   ├── settings.py                   ← Django settings
│   ├── urls.py                       ← URL routing (connects URLs to views)
│   ├── views.py                      ← Custom views (dashboard, home)
│   ├── views_entity.py               ← Entity-related views
│   ├── views_invoice.py              ← Invoice-related views
│   └── views_lists.py                ← List views (vendors, customers, etc.)
│
└── django_ledger/                    ← Django Ledger package
    ├── templates/                    ← ALL templates (original + custom)
    │   └── django_ledger/
    │       ├── base_shadcn.html      ← Custom base template
    │       ├── vendor/
    │       │   ├── vendor_list.html           ← Original (Bulma)
    │       │   └── vendor_list_shadcn.html    ← Custom (shadcn/ui)
    │       ├── customer/
    │       │   ├── customer_list.html         ← Original
    │       │   └── customer_list_shadcn.html  ← Custom
    │       ├── financial_statements/
    │       │   ├── balance_sheet.html         ← Original
    │       │   ├── balance_sheet_shadcn.html  ← Custom
    │       │   ├── income_statement.html      ← Original
    │       │   └── income_statement_shadcn.html ← Custom
    │       └── components/
    │           └── shadcn/
    │               └── sidebar_menu.html      ← Custom sidebar
    │
    └── views/                        ← Django Ledger's original views
        ├── vendor.py                 ← VendorModelListView (original)
        ├── customer.py               ← CustomerModelListView (original)
        └── financial_statement.py   ← Balance Sheet views (original)
```

## What's in `dev_env/`?

**Purpose:** Custom Python code that extends Django Ledger

### 1. `views_lists.py` (Custom Views)
```python
# Location: dev_env/views_lists.py

from django_ledger.views.vendor import VendorModelListView
from django_ledger.views.customer import CustomerModelListView
from django_ledger.views.financial_statement import FiscalYearBalanceSheetView

class VendorListShadcnView(VendorModelListView):
    template_name = 'django_ledger/vendor/vendor_list_shadcn.html'

class CustomerListShadcnView(CustomerModelListView):
    template_name = 'django_ledger/customer/customer_list_shadcn.html'

class BalanceSheetShadcnView(FiscalYearBalanceSheetView):
    template_name = 'django_ledger/financial_statements/balance_sheet_shadcn.html'
    # ... custom methods ...
```

**What it contains:**
- `VendorListShadcnView` - Extends Django Ledger's vendor list view
- `CustomerListShadcnView` - Extends Django Ledger's customer list view
- `BankAccountListShadcnView` - Extends Django Ledger's bank account list view
- `InvoiceListShadcnView` - Extends Django Ledger's invoice list view
- `BillListShadcnView` - Extends Django Ledger's bill list view
- `BalanceSheetShadcnView` - Extends Django Ledger's balance sheet view
- `IncomeStatementShadcnView` - Extends Django Ledger's income statement view

**Total:** ~200 lines of Python code

### 2. `urls.py` (URL Routing)
```python
# Location: dev_env/urls.py

from django.urls import path, include
from .views_lists import (
    VendorListShadcnView,
    CustomerListShadcnView,
    BalanceSheetShadcnView,
    # ... other imports ...
)

urlpatterns = [
    # Custom modernized routes
    path('entity/<slug:entity_slug>/vendors-shadcn/', 
         VendorListShadcnView.as_view(), 
         name='vendor-list-shadcn'),
    
    path('entity/<slug:entity_slug>/customers-shadcn/', 
         CustomerListShadcnView.as_view(), 
         name='customer-list-shadcn'),
    
    path('entity/<slug:entity_slug>/balance-sheet-shadcn/<int:year>/', 
         BalanceSheetShadcnView.as_view(), 
         name='balance-sheet-shadcn'),
    
    # Include Django Ledger's original URLs
    path('', include('django_ledger.urls', namespace='django_ledger')),
]
```

**What it contains:**
- Custom URL routes for modernized views
- Includes Django Ledger's original URLs
- Maps URLs to view classes

**Total:** ~150 lines

### 3. `settings.py` (Django Configuration)
```python
# Location: dev_env/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ...
    'django_ledger',  # Django Ledger app
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Django auto-discovers templates in app directories
        'APP_DIRS': True,  # Enable app template directories
        # ...
    },
]
```

**What it contains:**
- Django configuration
- Installed apps
- Database settings
- Template settings

**Total:** ~100 lines

### Summary of `dev_env/`
- **Purpose:** Custom Python code
- **Contains:** Views, URLs, settings
- **Total Code:** ~450 lines of Python
- **Type:** Extension code (inherits from Django Ledger)

## What's in `django_ledger/templates/`?

**Purpose:** ALL templates (both original Django Ledger and our custom ones)

### Why Templates Are Here

Django Ledger is a Python package, and by convention, Django apps store their templates in `app_name/templates/app_name/`. So Django Ledger's templates are in:

```
django_ledger/templates/django_ledger/
```

When we create custom templates, we put them in the **same directory structure** so Django can find them. This is standard Django practice.

### Custom Templates We Created

```
django_ledger/templates/django_ledger/
├── base_shadcn.html                              ← Custom base template
├── components/
│   └── shadcn/
│       └── sidebar_menu.html                     ← Custom sidebar
├── vendor/
│   └── vendor_list_shadcn.html                   ← Custom vendor list
├── customer/
│   └── customer_list_shadcn.html                 ← Custom customer list
├── bank_account/
│   └── bank_account_list_shadcn.html             ← Custom bank account list
├── bills/
│   └── bill_list_shadcn.html                     ← Custom bill list
├── invoice/
│   └── invoice_list_shadcn.html                  ← Custom invoice list
├── entity/
│   ├── entity_dashboard_shadcn.html              ← Custom dashboard
│   └── home_shadcn.html                          ← Custom home page
└── financial_statements/
    ├── balance_sheet_shadcn.html                 ← Custom balance sheet
    └── income_statement_shadcn.html              ← Custom income statement
```

**Total:** ~20 custom template files, ~3,000 lines of HTML/CSS

### Why Not in `dev_env/templates/`?

We **could** create a `dev_env/templates/` directory and put our templates there, but:

1. **Django's template discovery** - Django looks for templates in `app_name/templates/app_name/`
2. **Consistency** - Keeping all templates in one place is cleaner
3. **Convention** - This is the standard Django way

## The Complete Picture

### Custom Code Locations

| Component | Location | Purpose | Lines of Code |
|-----------|----------|---------|---------------|
| **Views** | `dev_env/views_lists.py` | Custom view classes | ~200 |
| **URLs** | `dev_env/urls.py` | URL routing | ~150 |
| **Settings** | `dev_env/settings.py` | Django config | ~100 |
| **Templates** | `django_ledger/templates/` | HTML/CSS | ~3,000 |
| **Sidebar** | `django_ledger/templates/.../sidebar_menu.html` | Navigation | ~400 |
| **Base** | `django_ledger/templates/.../base_shadcn.html` | Base template | ~200 |

**Total Custom Code:** ~4,050 lines

### Django Ledger's Original Code (Untouched)

| Component | Location | Purpose |
|-----------|----------|---------|
| **Views** | `django_ledger/views/` | Original view classes |
| **Models** | `django_ledger/models/` | Database models |
| **Forms** | `django_ledger/forms/` | Form classes |
| **URLs** | `django_ledger/urls/` | Original URL routing |
| **Templates** | `django_ledger/templates/` | Original templates |

**Total Django Ledger Code:** ~50,000+ lines (untouched!)

## How They Work Together

### Example: Vendors List

1. **User clicks "Vendors"** in sidebar
2. **URL:** `/entity/sample-company-inc-b1a78xt2/vendors-shadcn/`
3. **Django checks:** `dev_env/urls.py`
4. **Finds route:** `path('entity/<slug:entity_slug>/vendors-shadcn/', VendorListShadcnView.as_view())`
5. **Loads view:** `dev_env/views_lists.py` → `VendorListShadcnView`
6. **View inherits from:** `django_ledger/views/vendor.py` → `VendorModelListView`
7. **View specifies template:** `'django_ledger/vendor/vendor_list_shadcn.html'`
8. **Django loads template:** `django_ledger/templates/django_ledger/vendor/vendor_list_shadcn.html`
9. **Template extends:** `django_ledger/templates/django_ledger/base_shadcn.html`
10. **Result:** Beautiful shadcn/ui vendor list!

## File Count Summary

### In `dev_env/` (Python Code)
```bash
$ ls -1 dev_env/*.py
dev_env/__init__.py
dev_env/asgi.py
dev_env/settings.py
dev_env/urls.py
dev_env/views.py
dev_env/views_entity.py
dev_env/views_invoice.py
dev_env/views_lists.py
dev_env/wsgi.py
```
**Total:** 9 Python files

### In `django_ledger/templates/` (Custom Templates)
```bash
$ find django_ledger/templates -name "*_shadcn.html" | wc -l
20
```
**Total:** 20 custom template files

## Why This Structure?

### Advantages

1. **Separation of Concerns**
   - Python code in `dev_env/`
   - Templates in `django_ledger/templates/`

2. **Django Conventions**
   - Follows Django's standard app structure
   - Templates auto-discovered by Django

3. **Maintainability**
   - Easy to find view code (in `dev_env/`)
   - Easy to find templates (in `django_ledger/templates/`)

4. **Non-Invasive**
   - Django Ledger's original code untouched
   - Our custom code clearly separated

5. **Scalability**
   - Easy to add new views (add to `views_lists.py`)
   - Easy to add new templates (add to `templates/`)

## Could We Move Everything to `dev_env/`?

**Yes, but it would be more complex:**

```
dev_env/
├── views_lists.py                    ← Views (already here)
├── urls.py                           ← URLs (already here)
└── templates/                        ← NEW: Templates
    └── django_ledger/                ← Need to recreate structure
        ├── vendor/
        │   └── vendor_list_shadcn.html
        └── ...
```

**Why we didn't:**
1. Django Ledger already has a `templates/` directory
2. Easier to keep all templates in one place
3. Standard Django convention

## Quick Reference

### To Add a New Modernized View

1. **Create view class** in `dev_env/views_lists.py`:
   ```python
   class MyNewView(OriginalDjangoLedgerView):
       template_name = 'django_ledger/path/my_new_template_shadcn.html'
   ```

2. **Add URL route** in `dev_env/urls.py`:
   ```python
   path('entity/<slug:entity_slug>/my-new-view/', MyNewView.as_view(), name='my-new-view'),
   ```

3. **Create template** in `django_ledger/templates/django_ledger/path/my_new_template_shadcn.html`:
   ```django
   {% extends 'django_ledger/base_shadcn.html' %}
   {% block content %}
       <!-- Your custom HTML -->
   {% endblock %}
   ```

### To Find Code

- **View logic:** Look in `dev_env/views_lists.py`
- **URL routing:** Look in `dev_env/urls.py`
- **Templates:** Look in `django_ledger/templates/django_ledger/`
- **Django settings:** Look in `dev_env/settings.py`

## Conclusion

**Code is split between two locations:**

1. **`dev_env/`** (Python)
   - Custom views that extend Django Ledger
   - URL routing
   - Django settings
   - ~450 lines of Python

2. **`django_ledger/templates/`** (HTML/CSS)
   - Custom shadcn/ui templates
   - Sidebar navigation
   - Base template
   - ~3,000 lines of HTML/CSS

This structure follows Django conventions, keeps code organized, and makes it easy to maintain and extend!
