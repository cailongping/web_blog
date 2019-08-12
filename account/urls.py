from django.urls import path, re_path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name="register"),  # 注册
    path('person/', views.person_center, name="person"), # 个人中心
]