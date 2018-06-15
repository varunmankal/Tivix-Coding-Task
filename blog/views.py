from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Postdata
from .forms import PostForm

# Create your views here.

# function to display all the existing posts.

def home(request):
	posts = Postdata.objects.order_by('-date') # returns all the existing posts present in the Postdata
	return render(request, 'index.html', {'posts' : posts})	#passing above posts variable for display to the index.html 
	
# If the request is GET, then it displays empty form
# If the request is POST, then it stores the details 
# and today's date in the Postdata.
	
def newpost(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.date = timezone.now()
			post.save()
			return redirect('detailpost',pk=post.pk)
	else:
		form = PostForm()
	return render(request,'post_edit.html', {'form': form})	
	
# displaying the full description of the desired post	
	
def detailpost(request,pk):
	post = get_object_or_404(Postdata,pk=pk)
# passing the post variable for display to the post_detail.html	
	return	render(request,'post_detail.html', {'post': post})	

# function to edit the post.
# First, it the display the post to edit (on GET request).
# After necessary changes were made then it will update 
# the changes in Postdata. (on POST request) .
# At last redirecting to the detailed view of the post. 
def post_edit(request,pk):
	post = get_object_or_404(Postdata,pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST,instance=post)
		if form.is_valid():
			# here commit=False allows not to save the post right away 
			# but after adding date. 
			
			post = form.save(commit=False)
			post.date = timezone.now()
			post.save()
			return redirect('detailpost',pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request,'post_edit.html', {'form': form})		