from django.shortcuts import render
from login.models import Account
from django.contrib import auth
from lesson_watching.models import LessonLOL,LessonOver,LessonBattle

# Create your views here.

def home(request):
    context = {}
    
    if request.user.is_authenticated:
        account = Account.objects.get(user=request.user)
        context.setdefault('nickname', account.nickname)
        context.setdefault('id', account.id)
    return render(request,'home.html',context)


def about_us(request):
    return render(request,'about_us.html')

def teacher_info(request):
    return render(request, 'teacher_info.html')