from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from .models import Commission, Comment


class CommissionListView(ListView):
    model = Commission
    template_name = "commissions/commissions_list.html"
    context_object_name = "commissions"


def commission_detail(request, commission_id):
    commission = get_object_or_404(Commission, id=commission_id)
    comments = Comment.objects.filter(commission=commission)
    return render(
        request,
        "commissions/commissions_detail.html",
        {"commission": commission, "comments": comments},
    )
