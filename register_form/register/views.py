from django.shortcuts import render

# Create your views here.
from . import models  

def registerUser(request):
	return render(request,'register.html',{})


def storeRegisterUser(request):
	userDetails = models.UserDetail()

	errors = [ ]

	if(request.method == 'POST'):
		userDetails.user_name = request.POST['username']
		userDetails.user_phone_no = request.POST['phone']
		userDetails.user_email = request.POST['email']
		userDetails.user_pass = request.POST['pwd']
		userDetails.user_conf_pass = request.POST['conf_pwd']
		
		if(len(userDetails.user_phone_no)!=10 or userDetails.user_phone_no.isnumeric()==False):
			errors.append('Please enter a valid 10 digit phone number.')

		elif(userDetails.user_name.isalnum()==False):
			errors.append('Please enter a valid user name.')

		elif(userDetails.user_pass != userDetails.user_conf_pass):
			errors.append('Password and Confirm Password are not same.')

		else:
			userDetails.save()	
			context_success_redirect = {
				'success' : 'Thank you, for registering with us... \n Now you can login below using the link.' 
			}
			return render(request,'success.html',context_success_redirect)

		return render(request, 'register.html', {'errors': errors})

