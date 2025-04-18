from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Commission


class CommissionListView(ListView):
    model = Commission
    template_name = "commissions/commissions_list.html"
    context_object_name = "commissions"


class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commissions/commissions_detail.html"
    context_object_name = "commission"
