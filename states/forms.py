from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction
from .models import State
from django.core.validators import RegexValidator

class StateForm(UserCreationForm):
    # email = forms.EmailField(label='Email', required=True)
    
    name = forms.CharField(
        label='State Name', max_length=250, required=True)

    address_line1 = forms.CharField(label='Address Line 1', max_length=250, required=False)
    
    address_line2 = forms.CharField(label='Address Line 2', max_length=250, required=False)
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
                                )
    
    contact_number = forms.CharField(label='Phone Number', max_length=17, required=True, validators=[phone_regex])
    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        # user.email = self.cleaned_data['email']
        user.save()
        state = State.objects.create(
            user=user,
            name = self.cleaned_data['name'],
            address_line1= self.cleaned_data['address_line1'],
            address_line2= self.cleaned_data['address_line2'],
            contact_number= self.cleaned_data['contact_number'],   
            )
        state.save()
        return user

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        
        # State name validation
        if State.objects.filter(name=name).exists():
            print("State already exists")
            raise forms.ValidationError(f'State with name : "{name}" already exists.')
        
        # Email Validations
        if User.objects.filter(email=email).exists():
            print("Email already exists")
            raise forms.ValidationError('User with Email already exists.')

