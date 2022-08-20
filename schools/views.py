from urllib import request
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .permissions import is_in_group_schools
from .forms import ClassForm, MealForm, StudentForm, SchoolForm,AddAttendenceForm
from django.utils import timezone
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, DetailView, UpdateView
from .models import IMage, Student, Class, School, Meal, Attendence
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import AddImageserializer, Attendanceserializer, Mealserializers, studentSerializers,AddAttendanceserializer
from photocalpro.modelfile2 import return_calories_proteins

# Create your views here.
@user_passes_test(is_in_group_schools, login_url='/')
@login_required
def dashboardView(request):
    return render(request, 'schools/index.html')


@user_passes_test(is_in_group_schools, login_url='/')
@login_required
def profileView(request):
    return render(request, 'schools/profile.html')


@user_passes_test(is_in_group_schools, login_url='/')
@login_required
def attendenceView(request):
    return render(request, 'schools/attendence.html')



@user_passes_test(is_in_group_schools, login_url='/')
@login_required
def update_profile_pic(request):
    myschool = request.user.schools
    print(request)
    if request.method == 'POST':
        form = SchoolForm(request.POST, request.FILES, instance=myschool)
        if form.is_valid():
            print(form)
            form.save()
            print('saved')
            return redirect('schools:profile')

    else:
        print('NO POST REQUEST')
        form = SchoolForm(instance=myschool)
        print(type(form))
        return render(request, 'schools/update_profile_pic.html', {'form': form})


class ClassCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Class
    form_class = ClassForm
    template_name = "schools/create_new_class.html"
    success_url: reverse_lazy('schools:dashboard')

    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        return cond1

    def form_valid(self, form):
        form.instance.school = self.request.user.schools
        print('this validity')
        return super().form_valid(form)


class ClassUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Class
    form_class = ClassForm
    template_name = "schools/update_class.html"
    # success_url = reverse_lazy('schools:dashboard')

    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        cond2 = self.request.user.schools.classes.filter(
            pk=self.kwargs['pk']).exists()
        return cond1 and cond2


@user_passes_test(is_in_group_schools, login_url='/')
@login_required
def ClassDeleteView(request, pk):
    getclass = get_object_or_404(Class, pk=pk)
    if request.user.schools.classes.filter(pk=pk).exists():
        getclass.delete()
        return HttpResponseRedirect(reverse('schools:manage_class'))
    else:
        return render(request, '403.html')


class ClassDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Class
    template_name = "schools/class_detail.html"
    context_object_name = 'class'

    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        cond2 = self.request.user.schools.classes.filter(
            pk=self.kwargs['pk']).exists()
        return cond1 and cond2

    def get_context_data(self, **kwargs):
        context = super(ClassDetailView, self).get_context_data(**kwargs)
        myclass = get_object_or_404(Class, pk=self.kwargs['pk'])
        context["student_list"] = myclass.students.all()
        return context


class ClassListView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    model = Class
    template_name = "schools/manage_class.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_list'] = self.request.user.schools.classes.all()
        return context

    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        return cond1


class MealDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Meal
    context_object_name = 'meal'
    template_name = "schools/meal_detail.html"

    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        cond2 = self.request.user.schools.meals.filter(
            pk=self.kwargs['pk']).exists()
        return cond1 and cond2


class MealCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Meal
    fields = '__all__'
    template_name = "schools/todays-meal.html"
    success_url: reverse_lazy('schools:dashboard')

    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        return cond1

    def form_valid(self, form):
        form.instance.school = self.request.user.schools
        print('this validity')
        return super().form_valid(form)


class StudentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "schools/register_new_students.html"

    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        return cond1

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['current_class'].queryset = self.request.user.schools.classes.all()
        return form

class StudentDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Student
    template_name = "schools/student_detail.html"
    context_object_name = 'student'
 
    def test_func(self):
        cond1 = is_in_group_schools(self.request.user)
        mystudent = get_object_or_404(Student, pk=self.kwargs['pk'])
        cond2 = mystudent.current_class.school.user == self.request.user
        return cond1 and cond2   
    
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "schools/update_student.html"
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['current_class'].queryset = self.request.user.schools.classes.all()
        return form

class AttendenceView(TemplateView):
    template_name = "schools/attendence.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form1 = AddAttendenceForm(self.request.user)
        context['form1'] = form1
        return context

def addAtt(request, date, myclass):
    thisclass = get_object_or_404(Class, pk=myclass)
    student_list = thisclass.students.all()
    print(student_list)
    existing_record = Attendence.objects.filter(date=date).filter(student__in= student_list)
    print(existing_record)
    new_record = []
    for student in student_list:
        if existing_record.filter(student=student).exists():
            new_record.append((student,'checked'))
        else:
            new_record.append((student, ''))
    print(new_record)
    
    if request.method == 'POST':
        
        data = request.POST
        print(data)
        print(list(data.items()))
        present_students_pk = []
        for x,y in data.items():
            if y == 'on':
                present_students_pk.append(int(x))
        print(present_students_pk)
        existing_record.delete()
        for pk in present_students_pk:
            student = get_object_or_404(Student, pk=pk)
            attend = Attendence(student=student, date=date)
            try:
                attend.save() 
                print(f"Added {attend}")
            except:
                print(f"Already Exists! {attend}")
            
        return redirect(reverse('schools:attendence')) 
    
    
    return render(
        request = request, 
        template_name = 'schools/add_attendence.html', 
        context = {
            'new_record':new_record,
            'student_list':student_list,
        }
    )

def redirect_to_add_attendenceView(request):
    if request.method == 'POST':
        data = request.POST
        date = data['date']
        print(date)
        myclass = data['myclass']
        print(type(myclass))
        return redirect(reverse('schools:addAtt',  kwargs={'date':date, 'myclass':myclass}))   


class register_stu(APIView):
    def post(self,request,*args, **kwargs) :
        print(request.data)
        serializer=studentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'profile created'},status=status.HTTP_201_CREATED)
        return Response({'msg':serializer.errors},status=status.HTTP_403_FORBIDDEN)
    
    def get(self,request,*args, **kwargs):
        return Response({'msg':'Hi ! You can proceed to Resgister'},status=status.HTTP_200_OK)
    
class Meal_add(APIView):
    def post(self,request,*args, **kwargs):
        data=request.data
        if data['calories'] and data['protiens']:
            serializer=Mealserializers(data=data)
            data['school']=17
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Your meal has been added!!!'},status=status.HTTP_201_CREATED)
            return Response({'some error':serializer.errors},status=status.HTTP_200_OK)
        else:
            data['school']=17
            calpro=return_calories_proteins(data['meal_pic'])
            print(data['meal_pic'])
            serializer=AddImageserializer(data=data)
            if serializer.is_valid():
                serializer.save()
                meal_pic=IMage.objects.all().latest()
                return Response({'calories':calpro['calories'],'proteins':calpro['proteins'],'name':data['name'],'meal_pic':meal_pic},status=status.HTTP_200_OK)
            return Response({'msg':serializer.errors},status=status.HTTP_200_OK)
        
        
    def get(self,request,*args, **kwargs):
        return Response({'msg':'yo user'},status=status.HTTP_200_OK)
    
class profile_get(APIView):
    def get(self,request,*args, **kwargs):
        cond1 = is_in_group_schools(self.request.user)
        print(self.kwargs['pk'])
        mystudent = Student.objects.get(id=self.kwargs['pk'])
        serialized_data=studentSerializers(mystudent)
        cond2 = mystudent.current_class.school.user == self.request.user
        print(serialized_data)
        return Response({'msg':serialized_data.data},status=status.HTTP_200_OK)
    
    def put(self,request,*args, **kwargs):
        data=request.data
        serializer=studentSerializers(id=self.kwargs['pk'],data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'successfully edited!!'},status=status.HTTP_200_OK)
        return Response({'msg':serializer.errors},status=status.HTTP_201_CREATED)
    
class attendance(APIView):
    def get(self,request,*args, **kwargs):
        stu=Student.objects.all()
        serializer=Attendanceserializer(stu, many=True)
        return Response({'msg':serializer.data},status=status.HTTP_200_OK)
    
    def post(self,request,*args, **kwargs):
        data=request.data
        if len(data['students'])==0:
            stu=Student.objects.filter(current_class=data['class'])
            serializer=Attendanceserializer(stu, many=True)
            ate=Attendence.objects.filter(date=data['date'])
            serializer_attend=AddAttendanceserializer(ate,many=True)
            return Response({'msg':{'classstudent':serializer.data,'alreadyaddedone':serializer_attend.data}},status=status.HTTP_200_OK)
        else:
            stu_list={}
            for item in data['students']:
                stu_list['student_id']=item
                stu_list['date']=data['date']
                print(stu_list)
                stu=Attendence(student_id=stu_list['student_id'],date=stu_list['date'])
                stu.save()
                    # return Response({'msg':serializer.data},status=status.HTTP_200_OK)
            return Response({'msg':'attenddance added!!'},status=status.HTTP_200_OK)