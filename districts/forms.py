from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction
from .models import District
from schools.models import School
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate, get_user_model, password_validation
import unicodedata
from django.core.exceptions import ValidationError
def _(something):
    return something

class UsernameField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize("NFKC", super().to_python(value))

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            "autocapitalize": "none",
            "autocomplete": "username",
        }

class SchoolForm(forms.ModelForm):
    
    username = UsernameField()
    
    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    
    class Meta:
        model = School
        exclude = ('user','district')

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            print(f"Username {username} already exists")
            raise forms.ValidationError(f'User with Username {username} already exists.')
        return username
    

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    
    @transaction.atomic
    def save(self):
        school = super().save(commit=False)
        user = User.objects.create_user(
            username=self.cleaned_data["username"], 
            email=self.cleaned_data["email"], 
            password=self.cleaned_data["password1"]
        )
        user.save()
        school.user = user
        school.save()
        return school
    