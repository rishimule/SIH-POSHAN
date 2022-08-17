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

class AddAttendenceForm(forms.Form):
    
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=True) 
    myclass = forms.ModelChoiceField(queryset=None, empty_label=None, required=True)
    
    def __init__(self,user, *args, **kwargs):
         super(AddAttendenceForm, self).__init__(*args, **kwargs)
         self.user = user
         print(self.user.schools.classes.all().order_by('class_name'))
         if self.user.schools.classes.all().exists():
            self.fields['myclass'].queryset = self.user.schools.classes.all().order_by('class_name')
