from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from .models import Commission, Job, JobApplication


class CommissionListView(ListView):
    model = Commission
    template_name = "commissions/commissions_list.html"
    context_object_name = "commissions"


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
