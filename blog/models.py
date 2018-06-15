from django.db import models

# Create your models here.

# creating a model to store title, description and date.
# Here, I assumed only one author. If there were multiple
# authors, then it is necessary to have a field for author name

class Postdata(models.Model):
	title = models.CharField(max_length=50, unique=True)
	description = models.TextField()
	date = models.DateField(auto_now_add = True)
	def __str__(self):
		return self.title