from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib import auth
from .models import Account

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['id']
        password = request.POST["password"]
        
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "회원정보가 일치하지 않습니다.")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST":
        user_id = request.POST.get('id')
        email = request.POST.get('email')
        nickname = request.POST.get('nickname')
        user_password1 = request.POST.get('password1')
        user_password2 = request.POST.get('password2')



        if user_id == ""or nickname =="" or email == "" or user_password1 == "" or user_password2 == "":
            messages.info(request,"모든 항목을 채워주세요.")
            return redirect('signup')
        
                # 비밀번호가 다를 때
        if not user_password1 == user_password2:
            messages.info(request, "비밀번호가 다릅니다.")
            return redirect('signup')

        
        user = User.objects.create_user(username=user_id, password=user_password1)
        user.save()
        account = Account(user=user, email=email, nickname=nickname)
        account.save()
        return redirect('home')
    else:
        return render(request, 'signup.html')


def info_change(request):
    if request.method == 'POST':
        this_account = Account.objects.get(user=request.user)
        old_password = request.POST.get("old_password")
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        new_nickname = request.POST.get("new_nickname")
        new_email = request.POST.get("new_email")
        user = request.user

        if check_password(old_password,user.password):
            if new_password1==new_password2:
                user.set_password(new_password1)
                this_account.nickname = new_nickname
                this_account.email = new_email
                user.save()
                this_account.save()
                auth.login(request,user)
                return redirect('home')
            else:
                messages.info(request, "비밀번호가 다릅니다.")
        else:
            messages.info(request, "기존 비밀번호를 확인하세요.")
    else: 
        return render(request,'info_change.html')