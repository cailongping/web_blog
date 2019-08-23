from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
from blog.models import Article
from .models import UserInfo
from .forms import RegisterForm, UserInfoForm, UserInfoRegisterForm, UserForm   # 引入forms.py中定义好的表单类

def register(request):
    if request.method != "POST":
        # Django自带的User模型的表单
        form = RegisterForm()
        # 自己通过一对一创建的用户表单
        user_info_form = UserInfoRegisterForm()
    else:
        form = RegisterForm(data=request.POST)
        user_info_form = UserInfoRegisterForm(data=request.POST)
        if form.is_valid() and user_info_form.is_valid():
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


@login_required(login_url='login')
def edit_phone(request):
    # 修改用户信息
    user = User.objects.get(username=request.user)
    user_info = user.userinfo
    if request.method != "POST":
        form = UserForm(instance=user)
        user_info_form = UserInfoForm(instance=user_info)
    else:
        user_info_form = UserInfoForm(request.POST, request.FILES, instance=user_info )
        form = UserForm(request.POST, instance=user)
        if user_info_form.is_valid() and form.is_valid():
            user_info.save()
            user.save()
            return redirect('account:person')     
    return render(request, 'account/edit_phone.html', locals())


@login_required(login_url='login')
def person_article(request):
    article_list = Article.objects.filter(author=request.user).order_by('pub_date')
    # print(article_list)
    return render(request, 'account/person_article.html', locals())

