from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.detail import DetailView
from .models import Commission, Comment


def commission_list(request):
    commissions = get_list_or_404(Commission)

    return render(
        request, "commissions/commissions_list.html", {"commissions": commissions}
    )


class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commissions/commissions_detail.html"
    context_object_name = "commission"
