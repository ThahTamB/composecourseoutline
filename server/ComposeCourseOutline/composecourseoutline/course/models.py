from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField

class User(AbstractUser):
    avatar = models.ImageField(upload_to='upload/%Y/%m')

class Major(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name

class ItemBase(models.Model):
    class Meta:
            abstract = True
    image = models.ImageField(upload_to='course/%Y/%m', default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class Category(models.Model):
    class Meta:
        unique_together = ('name','major')

    name = models.CharField(max_length=100, null=False, unique=True)
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class CourseOutline(models.Model):
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null= True)
    outline = models.ForeignKey('Outline', on_delete=models.SET_NULL, null=True)

class Course(ItemBase):
    #subject = models.CharField(max_length=100, null=True)
    description = RichTextField()
    #category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    schoolYear = models.CharField(max_length=100, null=False)
    #semester = models.CharField(max_length=100, null=False)
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True)
    outlines = models.ManyToManyField('Outline',through='CourseOutline', related_name='courses_included', blank=True)

    def __str__(self):
        return f"{self.schoolYear} - {self.major}"

class Outline(ItemBase):
    content = RichTextField()
    category = models.ForeignKey(Category, related_name="outlines", on_delete=models.SET_NULL, null=True)
    #course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    courses = models.ManyToManyField(Course, through='CourseOutline', related_name='outline_set', blank=True)
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.category.name

class Point(models.Model):
    type = models.CharField(max_length=100, default='Enter the grade type here', null=False)
    percent = models.DecimalField(max_digits=10, decimal_places=2)
    outline = models.ForeignKey(Outline, on_delete=models.CASCADE, null=True)

