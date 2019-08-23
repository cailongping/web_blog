from django.urls import path, re_path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name="register"),  # 注册
    path('person/', views.person_center, name="person"), # 个人中心
    path('edit_user/', views.edit_user, name="edit_user"), # 编辑用户信息
    path('person_article/', views.person_article, name="person_article"), # 查询当前登录用户已经发布的文章
]