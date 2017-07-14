#coding:utf-8
from django.shortcuts import render
from models import *
from django.http import JsonResponse
from django.db.models import Sum
from userinfo.user_decorators import islogin
from userinfo.models import UserInfo

# Create your views here.
@islogin
def cart(request):
    uid = request.session.get('user_id')
    carts = CartInfo.objects.filter(user_id=uid)
    context = {'title':'购物车','carts':carts}
    return render(request,'goods_cart/cart.html',context)

def add_goods(request):
    print '----------add--------'
    try:
        gid = request.GET.get('gid')
        count = int(request.GET.get('count','1'))
        uid = request.session.get('user_id')
        carts = CartInfo.objects.filter(user_id=uid,goods_id=gid)
        if len(carts)==0:
            cart = CartInfo()
            cart.goods_id = gid
            cart.user_id = uid
            cart.count = count
            cart.save()
        else:
            cart = carts[0]
            cart.count+=count
            cart.save()
        return JsonResponse({'isadd':1})
    except:
        print '--------add_defeated-------'
        return JsonResponse({'isadd':0})

def get_cart_count(request):
    uid = request.session.get('user_id')
    carts = CartInfo.objects.filter(user_id=uid)
    count = 0
    if len(carts)==0:
        count = 0
    else:
        for cart in carts:
            count += cart.count
    return JsonResponse({'count':count})

def cart_delete(request):
    try:
        cid= request.GET.get('cid')
        cart = CartInfo.objects.filter(id=cid)[0]
        cart.delete()
        return JsonResponse({'isdelete':1})
    except:
        return JsonResponse({'isdelete':0})

def cart_edit(request):
    try:
        cid = int(request.GET.get('cid'))
        count = int(request.GET.get('count'))
        cart = CartInfo.objects.get(pk=cid)
        cart.count=count
        cart.save()
        return JsonResponse({'ok':1})
    except:
        return JsonResponse({'ok':0})

def order(request):
    try:
        user_id = request.session.get('user_id')
        user = UserInfo.objects.get(pk=user_id)
        # print '--------order--------'
        # print user
        cid_list = request.POST.getlist('cid_list')
        cart_list = CartInfo.objects.filter(id__in = cid_list)
        context = {'user':user,'cart_list':cart_list,'title':'提交订单'}
        return render(request,'goods_cart/place_order.html',context)
    except:
        pass
        # print '--------error--------'
