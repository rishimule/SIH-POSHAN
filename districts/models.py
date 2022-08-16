from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator
from states.models import State
import os
from django.contrib.auth.models import Group
from merakiiextras.common import get_current_datetime
from slugify import slugify



# Create your models here.

def _(something):
    return something

def rename_upload_image_district_profile(instance, filename):
    ext = filename.split('.')[-1]
    filename = "profile/district/%s/%s/%s.%s.%s" % (instance.user, instance.name, filename, get_current_datetime(), ext)
    return (os.path.join('images/', filename))

class District(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='districts')
    name = models.CharField(max_length=150)
    email = models.EmailField( max_length=254)
    profile_pic= models.ImageField(blank=False, upload_to=rename_upload_image_district_profile)
    address_line1 = models.CharField( max_length=250)
    address_line2 = models.CharField( max_length=250)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
                                )
    contact_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='districts')
    

    class Meta:
        verbose_name = _("district")
        verbose_name_plural = _("districts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("district_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        u = self.user
        u.email = self.email
        u.save()
        my_group = Group.objects.get(name='districts') 
        my_group.user_set.add(self.user)
        print(self.user)
        return super(District, self).save(*args, **kwargs)
