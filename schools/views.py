from urllib import request
from pprint import pprint as pp
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .permissions import is_in_group_schools
from .forms import ClassForm, MealForm, MealForm2, StudentForm, SchoolForm,AddAttendenceForm, HealthRecordForm
from django.utils import timezone
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, DetailView, UpdateView
from .models import Student, Class, School, Meal, Attendence, MealImage, HealthRecord
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from photocalpro.modelfile2 import return_calories_proteins
from photocalpro.sample import run as return_calories_proteins_and_stuff
import datetime
from django.db.models import Count, Avg
from twilio.rest import Client as TwilioClient


# Create your views here.
@user_passes_test(is_in_group_schools, login_url='/')
@login_required
def dashboardView(request):
    school = request.user.schools
    todays_date = datetime.date.today()
    
    # MEALS SERVED MONTHLY
    meals_served_monthly = Attendence.objects.filter(student__current_class__school = school , date__in=Meal.objects.filter(date__lte = todays_date ,date__year = todays_date.year, date__month = todays_date.month, school = school).values('date')).count()
    
    # MEALS SERVED WEEKLY
    meals_served_weekly = Attendence.objects.filter(student__current_class__school = school , date__in=Meal.objects.filter(date__lte = todays_date , date__gte = todays_date - datetime.timedelta(days = 7),  school = school).values('date')).count()
     
    # TODAYS ATTENDENCE
    todays_attendence_percentage =  int(Attendence.objects.filter(date=todays_date, student__current_class__school = school).count()  / Student.objects.filter(current_class__school = school).count() * 100)
    
    # AVERAGE DAILY MEAL SERVED
    distinct_pairs_count = Attendence.objects.values('date','student').distinct().count()
    # print(distinct_pairs_count)
    # print(Attendence.objects.values('date','student').distinct())
    distinct_users_count = Attendence.objects.values('date').distinct().count()  
    # print(Attendence.objects.values('date').distinct()) 
    # print(distinct_users_count) 
    average_daily_meals_served = int(distinct_pairs_count / distinct_users_count)
    
    # BMI DONUT
    meal_list = request.user.schools.meals.order_by('-date').all()[:5]
    student_list = Student.objects.filter(current_class__school = school)
    UW, H, OW = 0,0,0
    for student in student_list:
        if student.bmi  < 18.5:
            UW += 1
        elif student.bmi < 24.9:
            H += 1
        else:
            OW +=1           
    chart_donut_data = [UW, H, OW ]
    
    # BAR GRAPH
    total_no_of_students = Student.objects.filter(current_class__school = school).count()
    attendence_for_week= Attendence.objects.filter(student__current_class__school = school , date__in=Meal.objects.filter(date__lte = todays_date , date__gte = todays_date - datetime.timedelta(days = 7),  school = school).values('date')).values('date')
    for aatt in attendence_for_week[:20]:
        pp(aatt)
        # pp(aatt.date)
        # pp(aatt.total)
    print(attendence_for_week)
     
    # CONTEXT
    context = {
        'meals_served_monthly': meals_served_monthly,
        'meals_served_weekly': meals_served_weekly,
        'todays_attendence_percentage' : todays_attendence_percentage,
        'average_daily_meals_served' : average_daily_meals_served,
        'meal_list' : meal_list,
        'chart_donut_data' :chart_donut_data,
        'total_no_of_students' :total_no_of_students,
        
    }
    
    return render(request, 'schools/index.html', context=context)


@user_passes_test(is_in_group_schools, login_url='/')
@login_required
def profileView(request):
    school = request.user.schools
    todays_date = datetime.date.today()
    
    # PRE PRIMARY PERCENTAGE
    pre_primary_meal_percentage = int(Attendence.objects.filter(student__current_class__school = school, student__current_class__class_std__lte = -1, student__current_class__class_std__gte=-2).count()  / Student.objects.filter(current_class__class_std__lte = -1, current_class__class_std__gte=-2).count() * 100)
    
    # LOWER PRIMARY PERCENTAGE
    lower_primary_meal_percentage = int(Attendence.objects.filter(student__current_class__school = school, student__current_class__class_std__lte = 4, student__current_class__class_std__gte=0).count()  / Student.objects.filter(current_class__class_std__lte = 4, current_class__class_std__gte=0).count() * 100)
    
    # UPPER PRIMARY PERCENTAGE
    upper_primary_meal_percentage = int(Attendence.objects.filter(student__current_class__school = school, student__current_class__class_std__lte = 11, student__current_class__class_std__gte=5).count()  / Student.objects.filter(current_class__class_std__lte = 11, current_class__class_std__gte=5).count() * 100)
    
        
    context = {
        'pre_primary_meal_percentage': pre_primary_meal_percentage,
        'lower_primary_meal_percentage': lower_primary_meal_percentage,
        'upper_primary_meal_percentage': upper_primary_meal_percentage,
    }
    return render(request, 'schools/profile.html',context=context)


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


class MealListView(TemplateView):
    template_name = "schools/meal_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meal_list"] = self.request.user.schools.meals.all()
        return context
    
    



def mealCreateView(request):
    # After Image Upload
    if request.method == 'POST' and request.FILES:
        print(request.POST)
        print(request.FILES)
        
        temp_meal_pic = MealImage(meal_pic = request.FILES['meal_pic'])
        temp_meal_pic.save()
        print(temp_meal_pic.meal_pic.url)
        
        health_data = return_calories_proteins(temp_meal_pic.meal_pic.url[1:])
        print(health_data)
        
        school = request.user.schools
        name = request.POST['name']
        date = request.POST['date']
        meal_pic = temp_meal_pic.meal_pic
        calories = float(health_data['calories'])
        proteins = float(health_data['proteins']) 
        # quantity_per_plate_primary   = round( 450 *100 / calories, 2)
        # quantity_per_plate_secondary = round( 750 *100 / calories, 2)
        # quantity = int(request.POST['quantity'])
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        
        if latitude=="0":
            return redirect('schools/location_not_found.html')
            
        
        mealinstance = Meal(
            school = school,
            name = name,
            date = date,
            # quantity = quantity,
            meal_pic= meal_pic,
            calories = calories, 
            proteins = proteins,
            latitude = latitude,
            longitude = longitude,
            # calories = calories,
            # proteins = proteins,
            # quantity_per_plate_primary = quantity_per_plate_primary,
            # quantity_per_plate_secondary = quantity_per_plate_secondary,
        
        )
        print(mealinstance)
        
        form = MealForm2(instance=mealinstance)
        context = {
            'form': form,
            'temp_meal_pic' : temp_meal_pic,
            'next_action_url' : reverse('schools:todays_meal')
        }
        return render(request, "schools/todays-meal.html", context)
        
    # After meal upload
    elif request.method == 'POST':
            print(request.POST)
            print(request.FILES)
            school = request.user.schools
            name = request.POST['name']
            date = request.POST['date']
            meal_pic = MealImage.objects.get(pk=request.POST['mealimage_id']).meal_pic
            calories = request.POST['calories']
            # quantity = request.POST['quantity']
            proteins = request.POST['proteins']
            latitude = request.POST['latitude']
            longitude = request.POST['longitude']
                      
            mealinstance = Meal(
                school = school,
                name = name,
                date = date,
                meal_pic= meal_pic,
                # quantity = quantity,
                calories = calories,
                proteins = proteins,
                latitude = latitude,
                longitude = longitude,
            )
            print(mealinstance)
            if Meal.objects.filter(date=date).filter(school=school).exists():
                print('Old Meal Record Found')
                Meal.objects.filter(date=date).filter(school=school).delete()
                print('Deleted Old Meal Record!')
            mealinstance.save()
            print(f"{mealinstance} added to database!")
            return redirect(reverse('schools:meal_detail', kwargs={'pk': mealinstance.pk}))
    
    # First Visit
    else:
        form = MealForm()
        context = {
            'form': form,
            'next_action_url' : reverse('schools:todays_meal')
        }
        return render(request, "schools/todays-meal.html", context)


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

def send_sms(body,to):
    client = TwilioClient(settings.TWILIO_SID, settings.TWILIO_TOKEN)
    message = client.messages.create(
                     body=body,
                     from_=settings.TWILIO_PHONE,
                     to=to
                 )
    print(message.sid)
    
    

def add_healthrecord(request,studentpk):
    student = get_object_or_404(Student, pk= studentpk)
    form = HealthRecordForm()
    if request.method == 'POST':
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            healthrecord = HealthRecord()
            healthrecord.student = student
            healthrecord.height = form.cleaned_data['height']
            healthrecord.weight = form.cleaned_data['weight']
            healthrecord.haemoglobin = form.cleaned_data['haemoglobin']
            healthrecord.cognitive_score = 100
            healthrecord.save()
            send_sms(
                body=f".\n\nThe health details of {student.first_name} {student.last_name} was updated on {healthrecord.datetime.date()}.\n Height = {healthrecord.height}, \n Weight = {healthrecord.weight}, \n Bmi = {round(healthrecord.bmi,2)}",
                to=healthrecord.student.contact_number
            )
            
            return redirect(reverse('schools:class_detail', kwargs={'pk':student.current_class.pk}))
    else:
        context={
            'form':form,
            'student':student,
        }
        
        return render(request,'schools/add_healthrecord.html', context=context)
    

class HealthRecordDetailView(DetailView):
    model = HealthRecord
    template_name = "schools/healthrecord_detail.html"
    context_object_name = 'healthrecord'



class AttendenceView(TemplateView):
    template_name = "schools/attendence.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form1 = AddAttendenceForm(self.request.user)
        context['form1'] = form1
        return context

def addAtt(request, date, myclass):
    thisclass = get_object_or_404(Class, pk=myclass)
    student_list = thisclass.students.order_by('first_name').all()
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
            'date' : date,
            'thisclass':thisclass,
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

