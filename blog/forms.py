from django import forms
from .models import Postdata, Userdata

# A form for a new post with fields: title and description

class PostForm(forms.ModelForm):

	title=forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control col-md-10','placeholder':'Enter Title'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control col-md-10','placeholder':'Enter Description'}))
	# refers to Postdata model,from which two fields are chosen to
	# be present in the form.

	class Meta:
		model = Postdata
		fields = ('title','description')

# A Signin form for a new user

class SignInForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))

	class Meta:
		model = Userdata
		fields = ('username','password')
