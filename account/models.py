from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    """Model definition for UserInfo."""

    author = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, verbose_name='用户')
    user_img = models.ImageField(upload_to='avatar/', blank=True, default="avatar/avatar.jpg", verbose_name="头像")
    user_desc = models.CharField('个性签名', max_length=50, blank=True, default='')
    user_content = models.TextField('个人介绍', blank=True, default='')
    phone = models.CharField('手机号', unique=True, max_length=11)
    add_date = models.DateField('注册日期', auto_now_add=True)

    class Meta:
        """Meta definition for UserInfo."""

        verbose_name = '用户中心'
        verbose_name_plural = verbose_name

    def __str__(self):
        """Unicode representation of UserInfo."""
        return self.author.username
