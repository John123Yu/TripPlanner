from django.shortcuts import render, HttpResponse, redirect
from models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    
    return render (request, 'LoginAndReg/index.html')

def register(request):
	error_messages = {}
	if request.method == "POST":
		result = User.registerMgr.userRegister(request.POST['name'], request.POST['userName'], request.POST['password'], request.POST['confirm_password'])
		if result[0]:
		    request.session['login'] = result[1].id
		    request.session['name'] = result[1].name
		    request.session['loginStatement'] = "You have successfully Registered"
		    return redirect(reverse('BeltExam:index'))
		else:
		    error_messages = result[1]
		    return render(request, 'LoginAndReg/index.html',  error_messages )
	else:
		pass

def login(request):
	error_messages = {}
	if request.method == "POST":
		result = User.loginMgr.login(request.POST['userName'], request.POST['password'])
		if result[0]:
			request.session['login'] = result[1].id
			request.session['name'] = result[1].name
			request.session['loginStatement'] = "You have successfully logged in"
			# messages.info(request, 'Three Credits remain')
			# messages.error(request, "Entered BLA BLA BLA")

			return redirect(reverse('BeltExam:index'))
		else:
			error_messages = result[1]
			return render(request, 'LoginAndReg/index.html',  error_messages )
	else:
		return redirect ('/')

