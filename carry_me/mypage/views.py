from django.shortcuts import render
from django.contrib import auth
from login.models import Account
from lesson_watching.models import LessonOver , LessonBattle, LessonLOL
from django.db.utils import OperationalError 
# Create your views here.
 
 
def showMypage(request):
    

    if request.user.is_anonymous:
        messages.info(request, "로그인이 필요한 서비스입니다.")
            
        return redirect("login")

    
    account = Account.objects.get(user=request.user)

        
    try:
        lessonsO = LessonOver.objects.filter( user = request.user )
        
    except OperationalError:
        lessonsO = None    
    try:
        lessonsB = LessonBattle.objects.filter( user = request.user )
        
    except OperationalError:
        lessonsB = None    
    try:
        lessonsL = LessonLOL.objects.filter( user = request.user )
        
    except OperationalError:
        lessonsL = None    
    context = {'account': account ,'over' : lessonsO, 'battle' : lessonsB, 'lol' : lessonsL}


    return render(request,"mypage.html",context)


    



     
