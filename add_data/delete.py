from schools.models import School, Class, Student
from districts.models import District

def del_class(num=1):
    for _ in range(num):
        print(f'Now Deleting -------> {_}')
        myclass = Class.objects.order_by('?').first()
        print(myclass)
        myclass.delete()
        print(f'Deleted')
        