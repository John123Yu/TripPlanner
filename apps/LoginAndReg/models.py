from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime
import bcrypt
from django.core.urlresolvers import reverse

class RegisterManager(models.Manager):
    def userRegister(self, name, userName, password, confirmPassword):
		errors = {}

		if len(name) < 3 or len(userName) < 3:
			errors['TwoCharacters'] = ("Name and username must be at least three characters")
		if len(password) < 1 or len(confirmPassword) < 1:
			errors['PasswordRequired'] = ("Password and confirm password is required")
		if len(password) < 8:
			errors['PasswordLength'] = ("Password needs to be at least 8 characters")
		if password != confirmPassword:
			errors['PasswordNonmatch'] = ("Confirm password must match password")
		if len(errors) is not 0:
		    return (False, errors)
		else:
			pw_bytes = password.encode('utf-8')
			hashed = bcrypt.hashpw(pw_bytes, bcrypt.gensalt())
			user = User.registerMgr.create(name = name, userName = userName, password = hashed)
			print user
			user.save()
			return (True, user)

class LoginManager(models.Manager):
	def login(self, userName, password):
		errors = {}

		try:
			user = User.loginMgr.get(userName = userName)
		except:
			user = 0

		if user != 0:
			hashed = user.password.encode('utf-8')
			pw_bytes = password.encode('utf-8')
			if bcrypt.hashpw(pw_bytes, hashed) == hashed:
				a = 1
			else:
				errors["IncorrectLogin"] = "Incorrect Password"
		else:
			errors["NoEmail"] = "Entered UserName Not in Database"
		if len(errors) is not 0:
			print "No"
			return (False, errors)
		else:
			return (True, user)


class User(models.Model):
	name = models.CharField(max_length=100)
	userName = models.CharField(max_length=100)
	password = models.CharField(max_length=250)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	registerMgr = RegisterManager()
	loginMgr = LoginManager()

