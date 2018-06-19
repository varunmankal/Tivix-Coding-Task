from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Postdata,Userdata
from .forms import PostForm, SignInForm

# Create your views here.


# function to register the new user, display all the existing posts and
# starts a new session for the user

def home(request):
	if request.method == "POST":
		form = SignInForm(request.POST)
		if form.is_valid():
			signininfo = form.save(commit=False)
			user = signininfo.username
			# storing the current user name in session to keep track of all the operations
			request.session['username']=signininfo.username
			# checking if the user already exists
			if Userdata.objects.filter(username=user).exists():
				print("user exists")
			else:
				newuser=Userdata()
				newuser.username=signininfo.username
				newuser.password=signininfo.password
				newuser.save()
	else:
		pass
	# displaying all the existing posts in reverse chronological order
	posts = Postdata.objects.order_by('-pk')
	return render(request, 'index.html', {'posts' : posts})	#passing above posts variable for display to the index.html


# function that handles creation of new post
# If the request is GET, then it displays empty form


def newpost(request):

	# If the request is POST, then it stores the user, post's details
	# and today's date in the Postdata.
	if request.method == "POST":
		# creating a form instance and populating its data  from the request.
		form = PostForm(request.POST)
		if form.is_valid():
			# storing the fields details in model but not save the model object yet.
			post = form.save(commit=False)
			#post.date = timezone.now()
			#getting the name of current user which we stored in home function.
			user=request.session.get('username')
			#getting all the details of the current user
			userinfo=Userdata.objects.get(username__exact=user)
			#assigning the current user detials to the user field which is a foreign key in postdata
			post.user=userinfo
			post.save()
			#redirecting to the detailed view of the post
			return redirect('detailpost',pk=post.pk)
	else:
		#if request is GET, then creating a form instance with empty fields
		form = PostForm()
	return render(request,'post_edit.html', {'form': form})


# displaying the title and description of the desired post

def detailpost(request,pk):
	post = get_object_or_404(Postdata,pk=pk)
	user = request.session.get('username')
# passing the post variable and user name  to the post_detail.html
# Here, user name is passed so that only the author of the post can able to edit.
	return	render(request,'post_detail.html', {'post': post, 'user':user})

# function to edit the post.
# First, it the display the post to edit (on GET request).
# After necessary changes were made then it will update
# the changes in Postdata. (on POST request) .
# At last redirecting to the detailed view of the post.
def post_edit(request,pk):
	post = get_object_or_404(Postdata,pk=pk)
	# if the request is POST, then store the updated version of the post.
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
		# populating the form with existing title and description
		form = PostForm(instance=post)
	return render(request,'post_edit.html', {'form': form})

# function to display empty signin form
def signin(request):
	if request.method == "GET":
		# flushing the user's session if one exists
		request.session.flush()
		form = SignInForm()
	return render(request,'login.html',{'form':form})
