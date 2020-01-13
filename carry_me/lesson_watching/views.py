from django.shortcuts import render,redirect
from .models import LessonBattle, LessonLOL, LessonOver

# Create your views here.

def lesson_page_lol(request):
    return render(request, 'lesson_watching_lol.html')

def lesson_page_battleground(request):
    return render(request, 'lesson_watching_battleground.html')

def lesson_page_overwatch(request):
    return render(request, 'lesson_watching_overwatch.html')




##############    동영상 보는 창      #################

def video_watching(request):
    return render(request, 'video_watching.html')