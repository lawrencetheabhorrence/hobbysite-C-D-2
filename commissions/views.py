from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    DeleteView,
    UpdateView,
    CreateView,
    ListView,
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Case, When, Value

from .models import Commission, Job, JobApplication
from user_management.models import Profile


class CommissionListView(ListView):
    model = Commission
    template_name = "commissions/commissions_list.html"
    context_object_name = "commissions"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["commissions"] = commission_sort_by_status(Commission.objects.all())
        context["applications"] = application_sort_by_commission_status(
            JobApplication.objects.all()
        )
        print(context)

        return context


class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commissions/commissions_detail.html"
    context_object_name = "commission"

    def post(self, request, *args, **kwargs):
        commission = self.get_object()

        if request.user.is_authenticated:
            job_app = JobApplication()
            job_exists = Job.objects.filter(pk=int(request.POST.get("job"))).exists()
            user_exists = Profile.objects.filter(
                pk=int(request.POST.get("applicant"))
            ).exists()

            if job_exists and user_exists:
                potential_job = Job.objects.get(pk=int(request.POST.get("job")))
                potential_applicant = Profile.objects.get(
                    pk=int(request.POST.get("applicant"))
                )
                application_exists = JobApplication(
                    job=potential_job, applicant=potential_applicant
                ).exists

                if not application_exists:
                    job_app.job = potential_job
                    job_app.applicant = potential_applicant
                    job_app.save()

            return redirect("commissions:commission_detail", pk=commission.pk)

        return HttpResponse("You must be logged in to comment", status=403)


class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    fields = ["title", "description", "status"]
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        commission = self.get_object()
        context["jobs"] = Job.objects.filter(commission=commission)
        return context


class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    fields = ["title", "description", "status"]
    template_name_suffix = "_create_form"

    def form_valid(self, form):
        commission = form.save(commit=False)
        commission.creator = self.request.user.profile
        commission.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form)
        return super().form_invalid(form)


class JobView(LoginRequiredMixin, DetailView):
    model = Job
    template_name = "commissions/job_detail.html"
    context_object_name = "job"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["manager"] = Commission.objects.get(
            pk=Job.objects.get(pk=self.kwargs["pk"]).commission.pk
        ).creator

        return context

    def post(self, request, *args, **kwargs):
        if "accept" in request.POST:
            app_id = request.POST.get("accept")
            application = get_object_or_404(JobApplication, id=app_id)
            application.accept_application()
            return HttpResponseRedirect(
                reverse(
                    "commissions:commission_detail",
                    kwargs={"pk": application.job.commission.pk},
                )
            )

        elif "reject" in request.POST:
            app_id = request.POST.get("reject")
            application = get_object_or_404(JobApplication, id=app_id)
            application.reject_application()
            return HttpResponseRedirect(
                reverse(
                    "commissions:commission_detail",
                    kwargs={"pk": application.job.commission.pk},
                )
            )

        else:
            # redirect to self if somehow neither button was detected
            return HttpResponseRedirect(self.request.path_info)


def commission_sort_by_status(queryset):
    order = ["Open", "Full", "Completed", "Discontinued"]
    return queryset.order_by(
        Case(
            When(status=order[0], then=Value(0)),
            When(status=order[1], then=Value(1)),
            When(status=order[2], then=Value(2)),
            When(status=order[3], then=Value(3)),
            default=Value(4),
        ),
        "-created_on",
    )


def application_sort_by_commission_status(queryset):
    order = ["Open", "Full", "Completed", "Discontinued"]
    return queryset.order_by(
        Case(
            When(job__commission__status=order[0], then=Value(0)),
            When(job__commission__status=order[1], then=Value(1)),
            When(job__commission__status=order[2], then=Value(2)),
            When(job__commission__status=order[3], then=Value(3)),
            default=Value(4),
        ),
        "-job__commission__created_on",
    )


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    fields = ["role", "manpower_required", "status"]
    template_name_suffix = "_create"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commission"] = Commission.objects.get(pk=self.kwargs["pk"])
        return context

    def get(self, request, *args, **kwargs):
        affected_commission = get_object_or_404(Commission, pk=self.kwargs["pk"])
        if request.user.profile != affected_commission.creator:
            return redirect(reverse_lazy("commissions:commission_list"))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        print(self.kwargs)
        job = form.save(commit=False)
        job.commission = Commission.objects.get(pk=self.kwargs["pk"])
        job.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        affected_commission = get_object_or_404(Commission, pk=self.kwargs["pk"])
        if (
            request.user.is_authenticated
            and request.user.profile != affected_commission.creator
        ):
            return redirect(reverse_lazy("commissions:commission_list"))
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return Commission.objects.get(pk=self.kwargs["pk"]).get_absolute_url()


class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    fields = ["role", "manpower_required", "status"]
    template_name_suffix = "_update"

    def get(self, request, *args, **kwargs):
        job = self.get_object()
        if request.user.profile != job.commission.creator:
            return redirect(reverse_lazy("commissions:commission_list"))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        job = self.get_object()
        if (
            request.user.is_authenticated
            and request.user.profile != job.commission.creator
        ):
            return redirect(reverse_lazy("commissions:commission_list"))
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        job = self.get_object()
        return Commission.objects.get(pk=job.commission.pk).get_absolute_url()


class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Job

    def get(self, request, *args, **kwargs):
        job = self.get_object()
        if request.user.profile != job.commission.creator:
            return redirect(reverse_lazy("commissions:commission_list"))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        job = self.get_object()
        if (
            request.user.is_authenticated
            and request.user.profile != job.commission.creator
        ):
            return redirect(reverse_lazy("commissions:commission_list"))
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        job = self.get_object()
        return Commission.objects.get(pk=job.commission.pk).get_absolute_url()
