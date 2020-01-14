"""carry_me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from main.views import home,about_us, teacher_info
from login.views import login,signup,logout, info_change
from lesson_watching.views import lesson_page_lol, lesson_page_battleground , lesson_page_overwatch,video_watching
from QnA.views import uploadQuestion ,showQuestion ,new , showQuestionDetail, createAnswer
from django.conf import settings
from django.conf.urls.static import static
from mypage.views import showMypage



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about_us',about_us,name='about_us'),
    path('teacher_info',teacher_info,name='teacher_info'),
    path('signup/',signup,name="signup"),
    path('login/',login,name='login'),
    path('logout/',logout,name="logout"),
    path('info_change/',info_change, name="info_change"),
    path('question/new/',new,name ="question"),
    path('question/create',uploadQuestion,name = "questionCreate"),
    path('question/<int:question_id>',showQuestionDetail,name ='detail'),
    path('question/answer/<int:question_id>',createAnswer,name = "createAnswer"),
    path('QnA/',showQuestion,name = "QnA"),
    path('mypage/',showMypage,name='mypage'),
    path('lesson_watching_lol/',lesson_page_lol,name="lesson_watching_lol"),
    path('lesson_watching_battleground/',lesson_page_battleground,name="lesson_watching_battleground"),
    path('lesson_watching_overwatch/',lesson_page_overwatch,name="lesson_watching_overwatch"),
    path('video_watching/', video_watching, name='video_watching'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)