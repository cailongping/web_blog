from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from .forms import RegisterForm, UserInfoForm

def register(request):
    if request.method != "POST":
        form = RegisterForm()
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