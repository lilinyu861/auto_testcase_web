from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    # 用户信息
    user_name = models.CharField(max_length=100, blank=False, verbose_name='user_name')
    user_email = models.EmailField(max_length=255, blank=False, verbose_name='email_address')
    user_phone = models.CharField(max_length=11, verbose_name='user_phone')
    user_password = models.CharField(max_length=16, verbose_name='user_password')

    def __str__(self):
        return self.user_name
