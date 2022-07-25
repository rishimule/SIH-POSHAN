from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator
from districts.models import District 
import os



# Create your models here.

def _(something):
    return something

def rename_upload_image_taluka_profile(instance, filename):
    ext = filename.split('.')[-1]
    filename = "profile/taluka/%s/%s/%s.%s" % (instance.user, instance.name,  filename, ext)
    return os.path.join('images/', filename)

class Taluka(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='talukas')
    name = models.CharField(max_length=150)
    profile_pic= models.ImageField(blank=False, upload_to=rename_upload_image_taluka_profile)
    address_line1 = models.CharField( max_length=250)
    address_line2 = models.CharField( max_length=250)
    pincode = models.PositiveIntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
                                )
    contact_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Taluka")
        verbose_name_plural = _("Talukas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Taluka_detail", kwargs={"pk": self.pk})
