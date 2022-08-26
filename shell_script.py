from add_data import add

from schools.models import Student,Attendence,Meal,Class

# add.add_attendence()     

# add.add_class(100)

# add.add_student(1500)

Student.objects.filter(current_class__school = Class.objects.filter(school__name__icontains='adarsh').order_by('?').first())