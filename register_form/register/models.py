from django.db import models

# Create your models here.

class UserDetail(models.Model):
	user_name = models.CharField(max_length=200)
	user_phone_no = models.CharField(max_length=10)
	user_email = models.CharField(max_length=200)
	user_pass = models.CharField(max_length=20)
	user_conf_pass = models.CharField(max_length=20)

