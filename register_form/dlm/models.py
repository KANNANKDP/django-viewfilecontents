from django.db import models
from datetime import datetime
import os

# Create your models here.
class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y%m%d')
    docdate_created = models.DateTimeField(default=datetime.now)	

    def get_extension(self):
    	name, extension = os.path.splitext(self.docfile.name)
    	return extension