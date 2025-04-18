from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, UpdateView
from .models import Commission, Job, JobApplication


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


class CommissionUpdateView(LoginRequiredView, UpdateView):
    model = Commission
    fields = ["title", "description", "status"]
    template_name_suffix = "_update_form"


class JobView(DetailView):
    model = Job
    template_name = "commissions/job_detail.html"
    context_object_name = "job"

    def post(self, request, *args, **kwargs):
        if "accept" in request.POST:
            app_id = request.POST.get("accept")
            application = get_object_or_404(JobApplication, id=app_id)
            application.accept_job()

        elif "reject" in request.POST:
            app_id = request.POST.get("reject")
            application = get_object_or_404(JobApplication, id=app_id)
            application.reject_job()

        else:
            # redirect to self if somehow neither button was detected
            return HttpResponseRedirect(self.request.path_info)
