from django.conf.urls import url, include # Notice we added include
from . import views

urlpatterns = [
	url(r'^$', views.index, name = "index"),
	url(r'^users$', views.register, name = "register"),
	url(r'^login$', views.login, name = "login"),
]
