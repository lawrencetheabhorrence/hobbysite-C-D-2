from django.forms import ModelForm
from .models import Commission, Job


class CommissionForm(ModelForm):
    class Meta:
        model = Commission
        fields = ["title", "description", "status"]


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ["role", "manpower_required", "status"]
