from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    """Model definition for UserInfo."""

    author = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, verbose_name='用户')
    phone = models.IntegerField('手机号', unique=True)
    add_date = models.DateField('注册日期', auto_now_add=True)

    class Meta:
        """Meta definition for UserInfo."""

        verbose_name = '用户中心'
        verbose_name_plural = verbose_name

    def __str__(self):
        """Unicode representation of UserInfo."""
        return self.author.username
