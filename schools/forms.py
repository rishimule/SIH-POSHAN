from django import forms
from .models import Class, Student, Meal, Attendence, School

class ClassForm(forms.ModelForm):
    
    class Meta:
        model = Class
        # fields = '__all__'
        exclude = ['school']

class StudentForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))    
    
    class Meta:
        model = Student
        fields = ("__all__")
        # exclude = ('current_class')

class MealForm(forms.ModelForm):
    
    class Meta:
        model = Meal
        fields = ("__all__")

class SchoolForm(forms.ModelForm):
    
    class Meta:
        model = School
        fields = ("profile_pic",)
        widgets = {
            'profile_pic':forms.FileInput
        }
