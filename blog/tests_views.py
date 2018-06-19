from django.test import TestCase, Client
from blog.models import Postdata
from django.urls import reverse
from django.utils import timezone
from blog.forms import PostForm

# Contains tests related to views.

# Here, client acts like a web browser with which one 
# can make requests. Thanks to Django for 
# providing such a great functionality.

client = Client()

class BlogCreateViewTest(TestCase):
	
	# function to setup fresh data which is executed 
	# only once for all tests present in this file.
	# here, it adds 10 posts to the Postdata so that
	# we can test various functionalities.
	def setUpTestData():
		number_of_posts = 10
		for post in range(number_of_posts):
			Postdata.objects.create(title='post Title %s' % post,
					description='post description %s' % post,
					date = 	timezone.now())
	
	
	
	# To test the functionality of newpost function in views.py
	# which stores the details of the post in Postdata.
	def testCreatePost(self):
		response = self.client.post('/create/',{'title' : 'AI could get 100 times more'+
		'energy-efficient with IBM’s new artificial synapses',
		'description': 'eural networks are the crown jewel of the AI boom. They' +
		' gorge on data and do things like transcribe speech or describe' +
		'images with near-perfect accuracy'})
		rec = Postdata.objects.latest('pk')
		self.assertTrue(rec.title, 'AI could get 100 times more'+
		'energy-efficient with IBM’s new artificial synapses')
	
	# To test the functionality of post_edit function in views.py
	# which enables to edit and save the updated post in Postdata.	
	def testEditPost(self):
		print("edit")
		response = self.client.get('/post/1/edit/')
		post = Postdata.objects.get(pk=1)
		post.description="22222"
		response = self.client.post('/post/1/')	
		post = Postdata.objects.get(pk=1)
		self.assertTrue(post.description,'22222')