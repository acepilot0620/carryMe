from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from login.models import Account
# Create your models here.

class LessonOver(models.Model):
    title = models.CharField(max_length=20)
    detail = models.CharField(max_length=50)
    game = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)
    teacher_img = models.ImageField(upload_to='image')
    upload_date = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(User, on_delete= models.CASCADE)

class LessonBattle(models.Model):
    title = models.CharField(max_length=20)
    detail = models.CharField(max_length=50)
    game = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)
    teacher_img = models.ImageField(upload_to='image')
    upload_date = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(User, on_delete= models.CASCADE)

class LessonLOL(models.Model):
    title = models.CharField(max_length=20)
    detail = models.CharField(max_length=50)
    game = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)
    teacher_img = models.ImageField(upload_to='image')
    upload_date = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(User, on_delete= models.CASCADE )

    