from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from blog.models import User

class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'size':'30'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'size':'30'}))
    usermail = forms.EmailField(widget=forms.TextInput(attrs={'size':'30'}))

def index(req):
    return render(req,'index.html', {})

def regit(req):
    if req.method == "POST":
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            usermail = uf.cleaned_data['usermail']
            user = User()
            user.username = username
            user.password = password
            user.usermail = usermail
            user.save()
            return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render(req,'regit.html',{'uf':uf})

def login(req):
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')
        users = User.objects.filter(username__exact=username, password__exact=password)
        if users:
            user = User.objects.get(username=username)
            urname = user.username
            req.session['username'] = urname
            return HttpResponseRedirect('/home/')
        else:
            return HttpResponseRedirect('/login/')
    return render(req,'login.html',{})

def home(req):
	username = req.session.get('username','anbody')

	return render(req,'home.html',{'username':username})

def logout(req):
	del req.session['username']
	return HttpResponseRedirect('/index/')
