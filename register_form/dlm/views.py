from django.shortcuts import render,redirect
from django.db.models import Count
from django.http import HttpResponse
# Create your views here.
from .models import Document
from register import models
from django.contrib import messages
import os
from datetime import datetime

def homePageView(request):
	return render(request,'home.html',{})

def dashPageView(request):
	if(request.session.has_key('log_in')==True):
		if(request.session['log_in']==True):
			# return HttpResponse('session is active now...')
			# data = models.UserDetail.objects.all()
			# user_data = {
			# 	'users' : data
			# 	,'name' : request.session['name']
			# }
			# return render(request,'dashboard.html',user_data)
			data = Document.objects.extra({'docdate_created' : "date(docdate_created)"}).values('docdate_created').annotate(created_count=Count('id'))

			
			if(request.method == 'POST'):
					newdoc = Document(docfile = request.FILES['myfile'])
					newdoc.save()
					messages.success(request, 'File Uploaded successfully...')
      				#return HttpResponseRedirect('/dashboard/'+in_username)
					return redirect('/dashboard/')
					
			documents = Document.objects.all()

			doc_data = {
				'documents' : documents,
				'name' : request.session['name'],
				'data' : data,
			}

			return render(request,'dashboard.html',doc_data)

	elif(request.session.has_key('log_in')==False):
		return redirect('/login/')

	else:
		return redirect('/login/')

def logout(request):
	if(request.session.has_key('log_in')==True):
		del request.session['log_in']
		del request.session['name']
		request.session.flush()
		request.session.modified = True
		return redirect('/login/')

def filedetails(request,date):
	if(request.session.has_key('log_in')==True):
		if(request.session['log_in']==True):
			data = Document.objects.filter(docdate_created__contains=(date))			
			file_data = {
				'data' : data,
			}
			return render(request,'filedetails.html',file_data)


	elif(request.session.has_key('log_in')==False):
		return redirect('/login/')

	else:
		return redirect('/login/')

def viewfilecontents(request,filename):
	if(request.session.has_key('log_in')==True):
		if(request.session['log_in']==True):
			file_path = "media/" + str(filename)
			file = open(file_path,'r')
			file_contents = file.read()

			file_data = {
				'file_contents' : file_contents
			}
			return render(request,'viewfilecontents.html',file_data)

	elif(request.session.has_key('log_in')==False):
		return redirect('/login/')

	else:
		return redirect('/login/')	