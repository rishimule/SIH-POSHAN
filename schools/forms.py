from django import forms
from .models import Class, Student, Meal, Attendence

class ClassForm(forms.ModelForm):
    
    class Meta:
        model = Class
        # fields = '__all__'
        exclude = ['school']

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ("__all__")
        # exclude = ('current_class')

class MealForm(forms.ModelForm):
    
    class Meta:
        model = Meal
        fields = ("__all__")


