from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_name = models.CharField(max_length=20)
    user_pwd = models.CharField(max_length=40)
    user_mail = models.CharField(max_length=20)
    receiver = models.CharField(max_length=20,default='')
    receiver_phone = models.CharField(max_length=11,default='')
    receiver_addr = models.CharField(max_length=100,default='')
    receiver_code = models.CharField(max_length=6,default='')