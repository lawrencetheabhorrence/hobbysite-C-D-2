from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import ThreadCategory, Thread
from django.urls import reverse
from .forms import ThreadForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from user_management.models import Profile


class ThreadListView(ListView):
    model = Thread
    template_name = "forum/index.html"
    context_object_name = "thread"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ThreadCategory.objects.all()
        
        return context
    

class ThreadDetailView(DetailView):
    model = Thread
    template_name = "forum/detail.html"
    context_object_name = "thread"


class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    template_name = "forum/thread_create.html"
    context_object_name = "thread"
    fields = ['title', 'category', 'entry']

    def form_valid(self, form):
        form.instance.author = Profile.objects.get(user=self.request.user)  
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ThreadCategory.objects.all()  
        return context

    def get_success_url(self):
        return reverse('thread_detail', kwargs={'pk': self.object.pk})  


class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    template_name = "forum/thread_update.html"
    context_object_name = "thread"
    fields = ['title', 'category', 'entry']

    def form_valid(self, form):
        form.instance.updated_on = timezone.now()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ThreadCategory.objects.all()  
        return context

    def get_success_url(self):
        return reverse('thread_detail', kwargs={'pk': self.object.pk})



   
