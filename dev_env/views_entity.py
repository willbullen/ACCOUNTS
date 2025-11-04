from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django_ledger.models import EntityModel
from django_ledger.forms.entity import EntityModelCreateForm


class EntityCreateShadcnView(LoginRequiredMixin, CreateView):
    """
    Modernized Entity Create View with shadcn/ui styling
    """
    template_name = 'django_ledger/entity/entity_create_shadcn.html'
    model = EntityModel
    form_class = EntityModelCreateForm
    
    def get_success_url(self):
        return self.object.get_dashboard_url()
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
