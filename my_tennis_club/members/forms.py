# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Member

# create a ModelForm
class MembersForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Member
		fields = [
			"shoe",
			"firstname",
			"lastname",
			"phone",
			"joined_date",
        ]
