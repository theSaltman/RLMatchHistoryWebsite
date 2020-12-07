from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title
		
class Csv(models.Model):

	def validate_file_extension(value):
		if not value.name.endswith('.csv'):
			return False			
	
	file_name = models.FileField(upload_to='csvs/', validators=[validate_file_extension])
	uploaded = models.DateTimeField(auto_now_add=True)
	#activated = models.BooleanField(default=False)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	

	
	def __str__(self):
		#return f"File id: {self.id}" 
		return self.author.username + f" File id: {self.id}"
