from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Commission, Comment


def commission_list(request):
    commissions = Commission.objects.all().order_by("-created_on")

    return render(request, "commissions_list.html", {"commissions": commissions})


def commission_detail(request, commission_id):
    commission = get_object_or_404(Commission, id=commission_id)
    comments = Comment.objects.filter(commission=commission)
    return render(
        request,
        "commissions_detail.html",
        {"commission": commission, "comments": comments},
    )


# Create your views here.
