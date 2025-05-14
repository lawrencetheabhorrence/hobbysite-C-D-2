from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Commission, Job, JobApplication


class CommissionListView(ListView):
    model = Commission
    template_name = "commissions/commissions_list.html"
    context_object_name = "commissions"


class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commissions/commissions_detail.html"
    context_object_name = "commission"


class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    fields = ["title", "description", "status"]
    template_name_suffix = "_update_form"

    def get(self, request, *args, **kwargs):
        affected_commission = get_object_or_404(Commission, pk=self.kwargs["pk"])
        if request.user.profile != affected_article.commission:
            return redirect(reverse_lazy("commissions:commission_list"))
        return super().get(request, *args, **kwargs)


class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    fields = ["title", "description", "status"]
    template_name_suffix = "_create_form"

    def form_valid(self, form):
        commission = form.save(commit=False)
        commission.creator = self.request.user.profile
        commission.save()
        return super().form_valid(form)


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
