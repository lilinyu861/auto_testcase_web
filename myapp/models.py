from django.db import models


class User(models.Model):
    # 用户信息
    user_name = models.CharField(max_length=100, blank=False, verbose_name='user_name')
    user_email = models.EmailField(max_length=255, blank=False, verbose_name='email_address')
    user_password = models.CharField(max_length=16, blank=False, verbose_name='user_password')

    def __unicode__(self):
        return self.user_name


# class Input(models.Model):
#     # 用户输入信息
#     type = models.CharField(max_length=100, blank=False, verbose_name='type')
#     max_len = models.IntegerField(max_length=50)
#     min_len = models.IntegerField(max_length=50)

    # def __unicode__(self):
    #     return self.type
