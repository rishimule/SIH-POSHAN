from dataclasses import fields
from rest_framework import serializers

from .models import IMage, Meal, Student,Attendence

class studentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
        
class Mealserializers(serializers.ModelSerializer):
    class Meta:
        model=Meal
        fields='__all__'
        
class Attendanceserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('first_name','last_name','roll_no','current_class')
        
     
class AddAttendanceserializer(serializers.ModelSerializer):
    class Meta:
        model=Attendence
        fields=('id','date','student_id')
        
class AddImageserializer(serializers.ModelSerializer):
    class Meta:
        model=IMage
        fields=('__all__')
           