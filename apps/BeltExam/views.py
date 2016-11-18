from django.shortcuts import render, HttpResponse, redirect
from models import Trip, Trip_Users
from ..LoginAndReg.models import User, LoginManager, RegisterManager
from django.core.urlresolvers import reverse
from django.db.models import Count 
from datetime import datetime

def index(request):
	user = User.registerMgr.get(id = request.session['login'])
	context = {
		'your_trips': Trip_Users.objects.filter(User_id = user.id), 
		'all_trips': Trip.objects.all(),
		'name': user.name
    }
	return render(request, 'BeltExam/index.html', context)

def addPlanDisplay(request):
	return render(request, 'BeltExam/addPlanDisplay.html')

def addPlan(request):
	errors = {}
	if len(request.POST['destination']) < 1 or len(request.POST['description']) < 1 or len(request.POST['fromDate']) < 1 or len(request.POST['toDate']) < 1:
		errors['emptyEntries'] = "All Fields must not be empty"
	try:
		fromDate_object = datetime.strptime(request.POST['fromDate'], '%Y-%m-%d')
		toDate_object = datetime.strptime(request.POST['toDate'], '%Y-%m-%d')
	except:
		errors['dateError'] = "Dates not in correct format"
		fromDate_object = datetime.today()
		toDate_object = datetime.today()
	if fromDate_object <= datetime.today() or toDate_object <= datetime.today():
		errors['futureDate'] = "Dates must be in the future"
	if fromDate_object >= toDate_object:
		errors['dateFailure'] = "Travel Date to must be after Travel Date from:"

	if len(errors) > 0:
		return render(request, 'BeltExam/addPlanDisplay.html', errors)
	else:
		user = User.registerMgr.get(id = request.session['login'])
		addTrip = Trip.objects.create(destination = request.POST['destination'], description = request.POST['description'], toDate = request.POST['toDate'], fromDate = request.POST['fromDate'], creater = user)
		addMany = Trip_Users.objects.create(User_id = user.id, trip_id = addTrip.id)
	return redirect(reverse('BeltExam:index'))

def join(request, id):
	counter = 0
	user = User.registerMgr.get(id = request.session['login'])
	allMany = Trip_Users.objects.filter(trip_id = id)
	for item in allMany:
		if item.User == user:
			counter += 1

	if counter > 0:
		pass
	else:
		Trip_Users.objects.create(User_id = user.id, trip_id = id)

	return redirect(reverse('BeltExam:index'))

def logout(request):
	request.session['login'] = 0
	return redirect(reverse('login:index'))

def displayTrip(request, id):
	trip = Trip.objects.get(id = id)
	context = {
		"trip": trip,
		"other_users": Trip_Users.objects.filter(trip_id = trip.id).exclude(User_id = trip.creater)
		# "other_users": trip.trip_users.User.all().exclude(creater = trip.creater)
	}
	return render(request, 'BeltExam/displayTrip.html', context)
