from django.shortcuts import render,redirect
from models import *
from django.http import JsonResponse
import datetime
from user_decorators import *
# Create your views here.
def login(request):
    cookie = request.COOKIES.get('uname','')
    print request.path

    return render(request,'userinfo/login.html',{'uname':cookie,'top':'1'})

def register(request):
    return render(request,'userinfo/register.html',{'top':'1'})
@islogin
def user_center_info(request):
    user = UserInfo.objects.filter(pk=request.session['user_id'])
    uname = user[0].user_name
    umail = user[0].user_mail
    return render(request,'userinfo/user_center_info.html',{'uname':uname,'umail':umail})
@islogin
def user_center_order(request):
    return render(request,'userinfo/user_center_order.html')
@islogin
def user_center_site(request):
    user = UserInfo.objects.get(pk=request.session['user_id'])
    # print user
    # print request.session['user_id']
    if request.method == 'POST':
        # print "----------'hello'-----------"
        post = request.POST
        receiver = post.get('receiver')
        rec_phone = post.get('rec_phone')
        rec_mail = post.get('rec_mail')
        rec_addr = post.get('rec_addr')
        user.receiver = receiver
        user.receiver_phone = rec_phone
        user.receiver_code = rec_mail
        user.receiver_addr = rec_addr
        user.save()
    return render(request,'userinfo/user_center_site.html',{'user':user})

def index(request):
    return render(request,'userinfo/index.html')

def register_handle(request):
    user = UserInfo()
    if request.method == 'POST':
        post = request.POST
        user.user_name = post.get('user_name')
        user.user_pwd = post.get('user_pwd')
        user.user_mail = post.get('user_email')
        user.save()
        return render(request,'userinfo/login.html')
    else:
        uname = request.GET.get('user_name')
        num = UserInfo.objects.filter(user_name = uname).count()
        return JsonResponse({'number':num})

def login_handle(request):
    uname = request.POST.get('user_name')
    upwd = request.POST.get('user_pwd')
    user = UserInfo.objects.filter(user_name = uname)
    name_remb = request.POST.get('name_remb','0')
    if len(user) != 0:
        if user[0].user_pwd == upwd:
            request.session['user_id'] = user[0].id
            request.session['uname'] = uname
            # print request.session['uname']
            path = request.session.get('pre_path','/')
            # print request.session['pre_path']
            response = redirect(path)
            if name_remb == '1':
                response.set_cookie('uname',uname,expires=datetime.datetime.now()+datetime.timedelta(days = 14))
            else:
                response.set_cookie('uname','',expires=-1)
            return response
        else:
            return render(request,'userinfo/login.html',{'type':'1'})
    else:
        return render(request,'userinfo/login.html',{'type':'0'})

def quit_login(request):
    request.session.flush()
    return redirect('/login/')


