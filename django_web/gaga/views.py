#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User
from service import main
from api import execl
#from django.utils import simplejson
import json
from django.views.decorators.csrf import csrf_exempt
from gaga.models import Fileserver
#验证用户是否登录的装饰器
def requires_login(view):
    def new_view(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return view(request, *args, **kwargs)
    return new_view
#表单
class UserForm(forms.Form):
    username = forms.CharField(max_length=100, label='用户名')
    password = forms.CharField(widget=forms.PasswordInput(), label='密码')
'''    def clean_password(self):
        password = self.cleaned_data['password']
        num_words = len(password.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message'''


#注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf':uf}, context_instance=RequestContext(req))

#登陆


def login(request):
    error = False
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 3600)
                return response
            else:
                #比较失败，还在login
                error = True

    else:
        uf = UserForm(initial={'username': '请输入用户名'})
    return render_to_response('newtem/sign-in.html', {'uf': uf, 'error': error}, context_instance=RequestContext(request))

#首页

def index(request):
#   localtime = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    username = request.COOKIES.get('username', '')
#    if username:
#        return HttpResponseRedirect('/')
    return render_to_response('newtem/index.html', {'username': username})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

#samba服务器管理
def samba(request):
    username = request.COOKIES.get('username', '')
#    if username:
#        return HttpResponseRedirect('/')
    return main.ssh(request)

#获取测试资源
def testresource(request):
    a = execl.get_execl()
    return render_to_response('newtem/resource.html', {'list': a})
#修改表格数据
def changetab(request,tab):

    return HttpResponse(tab)

@csrf_exempt
def json_data(request):
    #ob = Fileserver.objects.all().order_by('-id')

    ob = [{'disk_useage':1,'smb_status': 2,'raid_status':3,'test':4}, {'disk_useage':1,'smb_status': 2,'raid_status':3,'test':4}]
    jsondata = json.dumps(ob)
    return HttpResponse(jsondata,content_type='application/json')