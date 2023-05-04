from django.db import models

# Create your models here.

from django.core import validators


from django.contrib.auth.models import User

class Register(models.Model):
    
    user_name=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    ph_number=models.CharField(max_length=10) #validators=[validators.RegexValidator([6-9]\d{9})])
    profile=models.ImageField(upload_to='Pr_pics') 
    bg_pic=models.ImageField(upload_to='Bg_pics')
    aadhar_no=models.CharField(max_length=12,validators=[validators.MaxLengthValidator(15),validators.MinLengthValidator(8)])

    def __str__(self) -> str:
        return self.user_name.first_name

    
