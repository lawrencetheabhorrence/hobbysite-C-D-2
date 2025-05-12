from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ThreadCategory, Thread
from .forms import CommentForm


class ThreadListView(ListView):
    model = ThreadCategory
    template_name = "forum/index.html"
    context_object_name = "categories"


class ThreadDetailView(DetailView):
    model = Thread
    template_name = "forum/detail.html"
    context_object_name = "thread"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thread = self.get_object()

        context["related_threads"] = (
            Thread.objects.all().exclude(pk=thread.pk).filter(author=thread.author)[:2]
        )
        return context

    def post(self, request, *args, **kwargs):
        thread = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.thread = thread
            comment.author = request.user.profile
            comment.save()

        return redirect("forum:thread_detail", pk=thread.pk)


class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    template_name = "forum/thread_create.html"
    context_object_name = "thread"
    fields = ["title", "category", "entry"]

    def get_success_url(self):
        return reverse("forum:thread_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        thread = form.save(commit=False)
        thread.author = self.request.user.profile
        thread.save()
        return super().form_valid(form)


class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    template_name = "forum/thread_update.html"
    context_object_name = "thread"
    fields = ["title", "category", "entry"]

    def get_success_url(self):
        return reverse("forum:thread_detail", kwargs={"pk": self.object.pk})

    def get(self, request, *args, **kwargs):
        self.object = Thread
        context = super().get_context_data(**kwargs)
        affected_thread = get_object_or_404(Thread, pk=context["pk"])
        if request.user.profile != affected_thread.author:
            return HttpResponseRedirect(reverse_lazy("forum:index"))
        return super().post(request, *args, **kwargs)
