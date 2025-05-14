from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
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

    def post(self, request, *args, **kwargs):
        job = get_object_or_404(Job, pk=self.kwargs["pk"])
        JobApplication.objects.create(job=job, applicant=self.request.user.profile)
        return redirect(self.request.path_info)


class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    fields = ["title", "description", "status"]
    template_name_suffix = "_update"

    def get(self, request, *args, **kwargs):
        affected_commission = get_object_or_404(Commission, pk=self.kwargs["pk"])
        if request.user.profile != affected_commission.creator:
            return redirect(reverse_lazy("commissions:commission_list"))
        return super().get(request, *args, **kwargs)


class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    fields = ["title", "description", "status"]
    template_name_suffix = "_create"

    def form_valid(self, form):
        commission = form.save(commit=False)
        commission.creator = self.request.user.profile
        commission.save()
        return super().form_valid(form)


class JobView(DetailView):
    model = Job
    template_name = "commissions/job_detail.html"
    context_object_name = "job"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["applications"] = self.get_object().applications.filter(
            status=JobApplication.ApplicationStatusOptions.PENDING
        )
        return context

    def post(self, request, *args, **kwargs):
        if "accept" in request.POST:
            app_id = request.POST.get("accept")
            application = get_object_or_404(JobApplication, id=app_id)
            application.accept_application()

        elif "reject" in request.POST:
            app_id = request.POST.get("reject")
            application = get_object_or_404(JobApplication, id=app_id)
            application.reject_application()

        return HttpResponseRedirect(self.request.path_info)


class JobCreateView(CreateView):
    model = Job
    template_name_suffix = "_create"
    fields = ["role", "manpower_required"]

    def form_valid(self, form):
        commission_id = self.kwargs["pk"]
        job = form.save(commit=False)
        job.commission = get_object_or_404(Commission, pk=commission_id)
        job.save()
        return super().form_valid(form)


class JobUpdateView(UpdateView):
    model = Job
    template_name_suffix = "_update"
    fields = ["role", "manpower_required"]

    def get(self, request, *args, **kwargs):
        affected_job = get_object_or_404(Job, pk=self.kwargs["pk"])
        if request.user.profile != affected_job.commission.creator:
            return redirect(reverse_lazy("commissions:commission_list"))
        return super().get(request, *args, **kwargs)
