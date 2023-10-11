from django.db import models

from django.conf import settings
from datetime import date,datetime
import os

from cloudinary.models import CloudinaryField

import re

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=500)
    summary = models.CharField(max_length=5000)
    image = CloudinaryField('image')
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    github_link = models.URLField()
    linkedin_link = models.URLField()

    def create_profile(self):
        self.save()
    @classmethod
    def delete_profile(cls, id):
        cls.objects.filter(id=id).delete()
    @classmethod
    def update_profile(cls, id):
        cls.objects.filter(id=id).update()


    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=2000)
    published_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

class Experience(models.Model):
    designation = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    is_present = models.BooleanField(null=True,blank=True)
    responsibilities_1 = models.CharField(max_length=2000,default=None,blank=True)
    responsibilities_2 = models.CharField(max_length=2000,default=None,blank=True)
    company = models.CharField(max_length=200,default=None,blank=True)
    location = models.CharField(max_length=200,default=None,blank=True)


    def __str__(self):
        return self.designation


class Skill(models.Model):

    name = models.CharField(max_length=50)
    image = CloudinaryField('image')
    def __str__(self):
        return self.name


class Connection(models.Model):
    your_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.your_name


class Project(models.Model):

    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    github_link = models.CharField(max_length=2000)
    proj_link = models.CharField(max_length=2000 , null=True)
    tech_stack = models.CharField(max_length=500)
    image = CloudinaryField('image')

   

    def __str__(self):
        return self.title
