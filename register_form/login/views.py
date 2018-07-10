from django.shortcuts import render,redirect

from django.http import HttpResponse
# Create your views here.
from register import models

def loginUser(request):
	if(request.session.has_key('log_in')==True):
		if(request.session['log_in'] == True):
			# return HttpResponse('Session is already active...')
			return redirect("/dashboard/")
		else:
			return redirect("/login/")
	elif(request.session.has_key('log_in')==False):
		return render(request,"login.html",{})

def validateUser(request):
	if(request.session.has_key('log_in')==True):
		if(request.session['log_in'] == True):
			# return HttpResponse('Session is already active...')
			return redirect("/dashboard/")
		else:
			return redirect("/login/")
		
	elif(request.session.has_key('log_in')==False):
			if(request.method=='POST'):
				user_name = request.POST['username']
				user_pass = request.POST['pwd']
				try:
					data = models.UserDetail.objects.get(user_name=user_name)
				except models.UserDetail.DoesNotExist:
					data=None
					# return HttpResponse('User does not exist')	
					return render(request,'login.html',{'error':'User does not exist'})
				if(data.user_pass==user_pass):
					request.session['log_in']=True
					request.session['name']=user_name
					# return HttpResponse('Session has been created..')
					return redirect('/dashboard/')
				# return render(request,'failed.html',{'failed':'Not working'})
			else:
				return redirect('/login/')