from django import forms
from .models import Class, Student, Meal, Attendence

class ClassForm(forms.ModelForm):
    
    class Meta:
        model = Class
        fields = '__all__'

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ("__all__")

class MealForm(forms.ModelForm):
    
    class Meta:
        model = Meal
        fields = ("school","name", "date", "meal_pic")


