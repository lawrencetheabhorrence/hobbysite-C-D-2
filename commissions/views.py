from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Commission, Comment


@login_required
def commission_list(request):
    profile = request.user.profile
    own_commissions = get_list_or_404(profile.commissions)
    applications = get_list_or_404(profile.applications)
    commissions = get_list_or_404(Commission.objects.exclude(creator=profile))

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
