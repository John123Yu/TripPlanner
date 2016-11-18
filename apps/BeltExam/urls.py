from django.conf.urls import url, include # Notice we added include
from . import views

urlpatterns = [
	url(r'^$', views.index, name = "index"),
	url(r'^addPlan$', views.addPlan, name = "addPlan"),
	url(r'^addPlanDisplay$', views.addPlanDisplay, name = "addPlanDisplay"),
	url(r'^logout$', views.logout, name = "logout"),
	url(r'^join/(?P<id>\d+)$', views.join, name = "join"),
	url(r'^display/(?P<id>\d+)$', views.displayTrip, name = 'displayTrip')
]