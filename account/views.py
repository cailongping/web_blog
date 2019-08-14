from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
from .models import UserInfo
from .forms import RegisterForm, UserInfoForm   # 引入forms.py中定义好的表单类

def register(request):
    if request.method != "POST":
        # Django自带的User模型的表单
        form = RegisterForm()
        # 自己通过一对一创建的用户表单
        user_info_form = UserInfoForm() 
    else:
        form = RegisterForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get('password2'))
            new_user.save()
            new_user_info = user_info_form.save(commit=False)
            new_user_info.author = new_user
            new_user_info.save()
            return redirect('login')

    return render(request, 'registration/register.html', {'form':form, 'user_info_form':user_info_form})


@login_required(login_url='login')
def person_center(request):
    # 个人中心
    user = User.objects.get(username=request.user.username)
    return render(request, 'account/person_center.html')