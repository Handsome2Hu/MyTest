#coding=utf-8
from django.shortcuts import render
import qrcode
from django.utils.six import BytesIO
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