from django.contrib import admin
from .models import Category, Article, Tags, Comment   # 引入菜单模型类
# Register your models here.

admin.site.register(Category)   # 注册菜单类
admin.site.register(Article)   # 注册文章类
admin.site.register(Tags)   # 注册文章标签类

admin.site.register(Comment)   # 注册留言管理类
