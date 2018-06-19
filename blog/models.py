from django.db import models
# Create your models here.

# creating a model to store username and password of the users

class Userdata(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.username+"-"+self.password


# creating a model to store title, description and date and its corresponding user.


class Postdata(models.Model):

	user = models.ForeignKey(Userdata,on_delete=models.CASCADE,default=1)
	title = models.CharField(max_length=50, unique=True)
	description = models.TextField()
	date = models.DateField(auto_now_add = True)
	def __str__(self):
		return self.title+"-by-"+self.user.username
