from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
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
from merakiiextras.common import get_current_datetime

def _(something):
    return something

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
    profile_pic= models.ImageField(blank=False, upload_to=rename_upload_image_school_profile, default='images\profile\state\default\default_state.png', max_length=999)
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


class SchoolLevel(models.Model):

    name = models.CharField(_("Level"), max_length=200)
    school = models.ForeignKey(School, related_name='schoollevels', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("schoollevel")
        verbose_name_plural = _("schoollevels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("schoollevel_detail", kwargs={"pk": self.pk})



class Class(models.Model):
    class_std = models.IntegerField(choices=std_choices())
    class_name = models.CharField(max_length=50)
    year = models.IntegerField(choices=year_choices(), default=current_year)
    school = models.ForeignKey(School, on_delete=models.CASCADE,related_name='classes')

    class Meta:
        verbose_name = "class"
        verbose_name_plural = "clases"
        unique_together = ('class_name', 'year', 'school')

    def __str__(self):
        return f"{self.class_name} - ({self.school})"

    def get_absolute_url(self):
        return reverse("schools:class_detail", kwargs={"pk": self.pk})

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
    current_height = models.FloatField(blank=False, null=False, default=1),
    current_weight = models.FloatField(blank=False, null=False, default=1),
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', 
                                 message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed."
                                )
    contact_number = models.CharField(validators=[phone_regex], max_length=17, blank=False, null=False, default='+918828443231') # Validators should be a list
    created  = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, editable=False)
 
    

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"
        unique_together = ('current_class', 'gr_no',)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.gr_no}) ({self.current_class})"

    def get_absolute_url(self):
        return reverse("schools:student_detail", kwargs={"pk": self.pk})

    @property    
    def age(self):
        born = self.dob
        today = timezone.now()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Student, self).save(*args, **kwargs)
    
    @property
    def bmi(self):
        return 9.8
        # return float(self.current_weight / (float(self.current_height/100)**2))
    
    @property    
    def calculate_age(self):
        born = self.dob
        today = timezone.now()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def rename_upload_image_meals(instance, filename):
    ext = filename.split('.')[-1]
    filename = "meals/%s/%s/%s.%s.%s.%s.%s" % (instance.school, instance.date, instance.name, str(instance.date), filename, get_current_datetime(), ext)
    return os.path.join('images/', filename)


class HealthRecord(models.Model):
    
    datetime = models.DateTimeField(default=timezone.now, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="healthrecords")
    height = models.IntegerField(_("Height (in cm)"), blank=False, null=False)
    weight = models.IntegerField(_("Weight (in Kg)"), blank=False, null=False)
    haemoglobin = models.FloatField(_("Haemoglobin count"), blank=True, null=False, default=0)
    cognitive_score = models.IntegerField(_("Cognitive Test Score"), blank=False, null=False, default=0 ,validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])

    

    class Meta:
        verbose_name = _("healthrecord")
        verbose_name_plural = _("healthrecords")
        
    def save(self, *args, **kwargs):
        ''' On save, update in Student Record '''
        mystudent = self.student
        mystudent.current_height = self.height
        mystudent.current_weight = self.weight
        mystudent.save()
        return super(HealthRecord, self).save(*args, **kwargs)
    
    @property
    def bmi(self):
        return (self.weight / ((self.height / 100)**2))

    def __str__(self):
        return f"{self.student} --> {self.datetime}"

    def get_absolute_url(self):
        return reverse("healthrecord_detail", kwargs={"pk": self.pk})

class Meal(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='meals')
    name = models.CharField("Meal Name",max_length=999)
    date = models.DateField(default=timezone.now, blank=False, null=False)
    meal_pic= models.ImageField(blank=False, upload_to = rename_upload_image_meals)
    calories = models.FloatField(blank=True, null=True)
    proteins = models.FloatField(blank=True, null=True)
    # quantity = models.IntegerField(_("Quantity per plate (in grams)"), blank=False, null=False, default=100)
    latitude = models.CharField(_("Latitude"), blank=True, null=False, max_length=999)
    longitude =models.CharField(_("Longitude"), blank=True, null=False, max_length=999)
    # quantity_per_plate_primary = models.FloatField(_("Quantity to serve - Primary Students (in grams) "), blank=True, null=True)
    # quantity_per_plate_secondary = models.FloatField(_("Quantity to serve - Secondary Students (in grams)"), blank=True, null=True)

    class Meta:
        verbose_name = _("meal")
        verbose_name_plural = _("meals")
        unique_together = ('school','date')

    def __str__(self):
        return f"{self.name} ({self.date}) ({self.school.name})"

    def get_absolute_url(self):
        return reverse("meal_detail", kwargs={"pk": self.pk})

class Attendence(models.Model):
    # meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=timezone.now, blank=False, null=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendences")

    class Meta:
        verbose_name = _("attendence")
        verbose_name_plural = _("attendences")
        # unique_together = ('meal', 'student')
        unique_together = ('date', 'student')

    def __str__(self):
        return f"{self.student} ----> {self.date}"

    def get_absolute_url(self):
        return reverse("attendence_detail", kwargs={"pk": self.pk})


def rename_upload_image_meals_temp(instance, filename):
    ext = filename.split('.')[-1]
    filename = "temp_meals/%s.%s.%s" % (filename, get_current_datetime(), ext)
    return os.path.join('images/', filename)

class MealImage(models.Model):
    meal_pic= models.ImageField('Meal Pic',blank=False, upload_to = rename_upload_image_meals_temp)
    class Meta:
        verbose_name = _("mealimage")
        verbose_name_plural = _("mealimages")

    def __str__(self):
        return self.meal_pic.url

    def get_absolute_url(self):
        return reverse("mealimage_detail", kwargs={"pk": self.pk})



