from django import forms
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from .models import Transaction, Product, ProductType
from user_management.models import Profile


class UserField(forms.ModelChoiceField):
    """
    A custom field for the User. Since we can't edit this field but somehow have to also display the User by name and not PK, we had to create this field that validates Users by name instead of their primary key
    """

    def valid_value(self, value):
        return self.queryset.filter(value).exists()

    def to_python(self, value):
        try:
            super(UserField, self).to_python(value)
        except ValidationError:
            user = Profile.objects.filter(name=value)
            if not user.exists():
                raise ValidationError(
                    self.error_messages["invalid_choice"], code="invalid_choice"
                )
            else:
                return user.first()
        return Profile.objects.get(user=value)


class ProductCreator(forms.ModelForm):
    owner = UserField(queryset=Profile.objects.values_list("name"), required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs["user"]
        super().__init__(*args, **kwargs)
        self.fields["owner"].required = False
        # The only valid option is the logged in user
        self.fields["owner"].queryset = Profile.objects.filter(user=user)
        self.fields["owner"].widget = forms.TextInput(
            attrs={"readonly": "true", "value": user.profile.name}
        )

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {"stock": forms.NumberInput(attrs={"min": "1"})}
