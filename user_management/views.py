from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Profile, ProfileCreationForm


def update(request):

    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":

        profile.name = request.POST.get("new_name")
        profile.email_address = request.POST.get("new_email_address")
        profile.save()

    context = {"profile": profile}

    return render(request, "user_management/update.html", context)


class ProfileCreateView(FormView):
    template_name = "registration/register.html"
    form_class = ProfileCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
