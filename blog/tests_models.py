from django.test import TestCase
from django.urls import resolve
from blog.models import Postdata
# Create your tests here.

# Test cases to test urls and models. Django executes 
# only tests that start with "test".

class TestUrlsAndModels(TestCase):
	
	# function to setup fresh data which is executed 
	# only once for all tests present in this file.
	def setUpTestData():
		Postdata.objects.create(title='Global Warming',
		description='Global warming is a gradual increase')
		
	# To test the maximum length of the title	
	def test_title_length(self):
		post = Postdata.objects.get(pk=1)
		length = post._meta.get_field('title').max_length
		self.assertTrue(length,50)

	# To test whether a URL after resolving matches 
	# with the correct URL name
	
	def test_home_url(self):
		found = resolve("/home/")
		self.assertEqual(found.url_name,'home')

	def test_view_post_url(self):
		response = resolve('/post/2/')
		self.assertEqual(response.url_name,'detailpost')
	
	# To test whether a URL is directing to the correct page	
	def test_create_view_url(self):
		response = self.client.get('/create/')
		self.assertEqual(response.status_code,200)