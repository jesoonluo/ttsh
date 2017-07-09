#coding:utf-8
from django.shortcuts import render
from models import *
# Create your views here.
def index(request) :
    goodsinfo = []  #-->{'typeofgoods':,'new_list':,'click_list':}
    #查询分类对象
    #查询分类对象中最火，以及最新的四个对象
    typeofgoods = TypeofGoods.objects.all()
    for t1 in typeofgoods:
        nlist = t1.goodsinfo_set.order_by('-id')[0:4]
        clist = t1.goodsinfo_set.order_by('-gclick')[0:4]
        goodsinfo.append({'t1':t1,'nlist':nlist,'clist':clist})
    context = {'glist':goodsinfo,'title':'主页','chart_show':'2'}
    return render(request,'goodsinfo/index.html',context)

def detail(request):
    context={'title':'商品详情','chart_show':'2'}
    return render(request,'goodsinfo/detail.html',context)

def list(request):
    context = {'title': '商品列表','chart_show':'2'}
    return render(request,'goodsinfo/list.html',context)