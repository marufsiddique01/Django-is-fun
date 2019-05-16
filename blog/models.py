from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

	def __str__(self):
		return self.title

	title = models.CharField(max_length=100)
	content = models.TextField()

	date_posted = models.DateTimeField(default=timezone.now) 
#auto_new= true for the post when it's created > timezone is a default django library to use time

	author = models.ForeignKey(User, on_delete=models.CASCADE) 
'''for the author with individual users > by using models.cascade. on delete for if the user delete the post 
his posts will be deleted as well. one way string '''

	

