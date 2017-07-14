from django.db import models
from userinfo.models import UserInfo
from goodsinfo.models import GoodsInfo
# Create your models here.
class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo)
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()