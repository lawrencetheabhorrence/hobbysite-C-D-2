from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import DetailView
from .models import Commission, Comment


def commission_list(request):
    commissions = get_list_or_404(Commission)

    return render(
        request, "commissions/commissions_list.html", {"commissions": commissions}
    )


def commission_detail(request, commission_id):
    commission = get_object_or_404(Commission, id=commission_id)
    comments = Comment.objects.filter(commission=commission)
    return render(
        request,
        "commissions/commissions_detail.html",
        {"commission": commission, "comments": comments},
    )


class JobView(DetailView):
    model = Job
    template_name = "commissions/job_detail.html"
