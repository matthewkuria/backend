# Create your models here.
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.models import CustomUser

memberships =[('regular','Regular'),('associate','Associate'), ('guest', 'Guest')]
maritals = [('single','Single'), ('married','Married'),('divorced','Divorced'), ('widowed', 'Widowed')]
genders=[('male','Male'),('female','Female')]
depts=[('Protocol','Protocol'),('worship','Praise & Worship'),('prayers','Prayer & Intercessory'),
('media','Media & Publicity'),('pastoral','Pastoral'),('evangelism','Evangelism'),('discipleship','Discipleship'),('youth','Youth'),('children','Children'),('men','Men'),('women','Women'),('mercy','Mercy Team'),('church_care','Church Care'),('missions','Missions')]
baptised= [('yes','Yes'),('no','No')]

class Fan(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,default=None,blank=True, null=True)
    full_name=models.CharField(max_length=30, default=None)
    membership = models.CharField(max_length=20, choices=memberships, default="regular")
    dob= models.DateField(default=None,blank=True, null=True)
    gender=models.CharField(max_length=10, choices=genders,default='male')
    mobile = models.CharField(max_length=40,null=True)
    date_joined= models.DateField(auto_now_add=True)
    status=models.BooleanField(default=False) 
    def __str__(self):
        return self.full_name


