#coding=utf-8
from django.shortcuts import render
import qrcode
from django.utils.six import BytesIO
from django import forms
from . import models

# Create your views here.

from django.http import HttpResponse

def index(request):
    articles = models.Article.objects.all()
    return render(request,"home.html",{'articles':articles})
    #return render(request,"home.html")

def add2(request):
    return HttpResponse("想复仇？你还嫩着！！")

def generate_qrcode(request):
    img = qrcode.make("http://weiwho.xin:8000/2")
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()
 
    response = HttpResponse(image_stream, content_type="image/png")
    return response

def add3(request):
    return HttpResponse('''
	<h1><center>扫码了你也是猪精</center></h1>
	''')

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog.html',{'article' : article})

def edit_page(request):
    return render(request,'blog_edit_page.html')

def edit_action(request):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    models.Article.objects.create(title=title,content=content)
    articles = models.Article.objects.all()
    return render(request,"home.html",{'articles':articles})
    
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    nickname = forms.CharField(label='昵称',max_length=50)
    email = forms.EmailField(label='邮箱')
    
def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            filterResult = models.User.objects.filter(username=username)
            if  len(filterResult) >0:
                return HttpResponse('用户名已存在')
            password = userform.cleaned_data['password']
            nickname = userform.cleaned_data['nickname']
            email = userform.cleaned_data['email']
            
            models.User.objects.create(username=username,password=password,nickname=nickname,email=email)
            
            return HttpResponse('注册成功！')
        
    else:
        userform = UserForm()
    return render(request,'regist.html',{'userform':userform})

def loging(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            
            user = models.User.objects.filter(username__exact=username,password__exact=password)
            
            if user:
                return render('home.html',{'userform':userform})
            else:
                return HttpResponse('用户名或密码错误，请重新登录')
            
        else:
            userform = UserForm()
        return render('login.html',{'userform':userform})