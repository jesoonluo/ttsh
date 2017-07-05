from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'userinfo/login.html')

def register(request):
    return render(request,'userinfo/register.html')

def user_center_info(request):
    return render(request,'userinfo/user_center_info.html')