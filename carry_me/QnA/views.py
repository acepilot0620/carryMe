from django.shortcuts import render, redirect
from django import forms
import getpass
from .models import Question ,Answer
from django.db import models    
from login.models import Account
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.utils import OperationalError 
from django.views import generic 
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def new(request):
    return render(request, 'question.html')

def uploadQuestion(request):

   
    if request.user.is_anonymous:
        messages.info(request, "로그인이 필요한 서비스입니다.")
            
        return redirect("login")

    question = Question()
        
    question.title = request.GET['title']
    question.content = request.GET['content']
    question.username = getpass.getuser()

    question.save()
    Question.objects.order_by('created_at').values()

    return redirect('/question/'+str(question.id))  
    

def showQuestion(request):

    

    try:
        listQuestions = {
            'question' :  Question.objects.all()

        }
        return render(request,"QnA.html",listQuestions)
        
    except OperationalError:
        return render(request,"QnA.html")        






    
def showQuestionDetail(request,question_id):
    
    question_detail = get_object_or_404(Question, pk =question_id)

    try:

        question_answer = Answer.objects.filter(question=question_detail)
        context = {'question': question_detail,
                'answer' : question_answer
                }

        return render(request, 'detail.html',context)
    except OperationalError:
        context = {'question': question_detail,
                }
        return render(request, 'detail.html',context)

    




def createAnswer(request, question_id):

   
    if request.user.is_anonymous:
        messages.info(request, "로그인이 필요한 서비스입니다.")
            
        return redirect("login")

    nickname = Account.objects.get( user = request.user).nickname
    
    question =get_object_or_404(Question, pk = question_id)
    answer = Answer(username = nickname  , question = question, content = request.GET['content'])
    
    answer.save()

    return redirect('/question/'+str(question.id))
