from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator
from talukas.models import Taluka
from districts.models import District
import os
import re
from django.contrib.auth.models import Group
from slugify import slugify

def _(something):
    return something

def get_current_datetime():
    """Returns alphanumeric datetime.

    Returns:
        str: alphanumeric DateTime
    """     
    return make_to_alphanumeric(datetime.now())

def make_to_alphanumeric(mystr):
    """Make a string in form of alphanumeric. 

    Args:
        mystr (str): String or something that can be converted to string

    Returns:
        str: alphanumeric output str
    """
    return re.sub('[\W_]+', '', str(mystr))

def year_choices():
    choices = [(r,r) for r in reversed(range(1990, timezone.now().year+2))]
    # choices = choices.reverse()
    return choices

def current_year():
    return timezone.now().year+1

def std_choices():
    choices = [(-2, 'Jr. KG'),(-1, 'Sr. KG')]
    choices.extend([(r,r) for r in range(1,9)])
    return choices

def rename_upload_image_school_profile(instance, filename):
    ext = filename.split('.')[-1]
    filename = "profile/school/%s/%s/%s.%s.%s.%s" % (instance.user, instance.name, instance.udise_code, filename, get_current_datetime(), ext)
    return (os.path.join('images/', filename))

class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='schools')
    email = models.EmailField( max_length=254)
    name = models.CharField(max_length=150)
    udise_code = models.CharField(max_length=150, unique=True)
    profile_pic= models.ImageField(blank=False, upload_to=rename_upload_image_school_profile)
    # ADDRESS
    address_line1 = models.CharField( max_length=250)
    address_line2 = models.CharField( max_length=250)
    pincode = models.PositiveIntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='schools')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
                                )
    contact_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    
    
    class Meta:
        verbose_name = "school"
        verbose_name_plural = "schools"

    def __str__(self):
        return f"{self.name} - ({self.district})"

    def get_absolute_url(self):
        return reverse("school_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        
        u = self.user
        u.email = self.email
        u.save()
        my_group = Group.objects.get(name='schools') 
        my_group.user_set.add(self.user)
        print(self.user)
        return super(School, self).save(*args, **kwargs)

class Class(models.Model):
    class_std = models.IntegerField(choices=std_choices())
    class_name = models.CharField(max_length=50, unique=True)
    year = models.IntegerField(choices=year_choices(), default=current_year)
    school = models.ForeignKey(School, on_delete=models.CASCADE,related_name='classes')

    class Meta:
        verbose_name = "class"
        verbose_name_plural = "clases"
        unique_together = ('class_name', 'year', 'school')

    def __str__(self):
        return f"{self.class_name} - ({self.school})"

    def get_absolute_url(self):
        return reverse("class_detail", kwargs={"pk": self.pk})

class Student(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    	)

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150, blank=True, null=True)
    father_name = models.CharField(max_length=150, blank=True, null=True)
    dob = models.DateField()
    current_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')
    gr_no = models.CharField(max_length=50)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, blank=False, default=0)
    current_height = models.FloatField(blank=True, null=True)
    current_weight = models.FloatField(blank=True, null=True)
    # age = models.IntegerField(blank=True, null=True)
    created  = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"
        unique_together = ('current_class', 'gr_no',)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.gr_no}) ({self.current_class})"

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})

    def get_queryset(self, *args, **kwargs):
        qs = super(Student, self).get_queryset().annotate(age=int(self.calculate_age(self)))
        return qs
        
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Student, self).save(*args, **kwargs)
    
    @property    
    def calculate_age(self):
        born = self.dob
        today = timezone.now()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def rename_upload_image_meals(instance, filename):
    ext = filename.split('.')[-1]
    filename = "meals/%s/%s/%s.%s.%s.%s.%s" % (instance.school, instance.date, instance.name, str(instance.date), filename,get_current_datetime(), ext)
    return os.path.join('images/', filename)

class Meal(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField("Meal Name",max_length=150)
    date = models.DateField(default=timezone.now, blank=False, null=False)
    meal_pic= models.ImageField(blank=False, upload_to = rename_upload_image_meals)
    calories = models.FloatField(blank=True, null=True)
    proteins = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = _("meal")
        verbose_name_plural = _("meals")
        unique_together = ('school','date')

    def __str__(self):
        return f"{self.name} ({self.date}) ({self.school.name})"

    def get_absolute_url(self):
        return reverse("meal_detail", kwargs={"pk": self.pk})

class Attendence(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("attendence")
        verbose_name_plural = _("attendences")
        unique_together = ('meal', 'student')

    def __str__(self):
        return f"{self.student} ----> {self.meal.date}"

    def get_absolute_url(self):
        return reverse("attendence_detail", kwargs={"pk": self.pk})




