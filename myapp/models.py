from django.db import models


class User(models.Model):
    # 用户信息
    user_name = models.CharField(max_length=100, blank=False, verbose_name='user_name')
    user_email = models.EmailField(max_length=255, blank=False, verbose_name='email_address')
    user_password = models.CharField(max_length=16, blank=False, verbose_name='user_password')

    def __unicode__(self):
        return self.user_name


class Interface(models.Model):
    # 接口测试数据库
    request_method = models.CharField(max_length=10, blank=False, verbose_name='request_method')
    interface_url = models.URLField(max_length=100, blank=False, verbose_name='interface_url')
    header_name = models.CharField(max_length=100, verbose_name='header_name')
    header_value = models.CharField(max_length=100, verbose_name='header_value')
    para_name = models.CharField(max_length=100, blank=True, verbose_name='parameter_name')
    para_value = models.CharField(max_length=100, blank=True, verbose_name='parameter_value')
    encryption_algorithm = models.CharField(max_length=60, blank=True, verbose_name='encryption_algorithm')

    def __unicode__(self):
        return self.interface_url

