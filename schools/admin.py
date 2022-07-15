from django.contrib import admin

from .models import School, Class, Student, Attendence, Meal

# Register your models here.
admin.site.register(School)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Attendence)
admin.site.register(Meal)