from django import forms
from .models import Postdata

# A form for a new post with fields: title and description

class PostForm(forms.ModelForm):
	
	# refers to Postdata model,from which two fields are chosen to
	# be present in the form.
	
	class Meta:
		model = Postdata
		fields = ('title','description')