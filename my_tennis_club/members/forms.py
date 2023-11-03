from django import forms
from .models import Member

class MembersForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            "shoe",
            "firstname",
            "lastname",
            "phone",
            "joined_date",
        ]

    # Add CSS classes to the widget attributes
    widgets = {
        "shoe": forms.TextInput(attrs={'class': 'p'}),
        "firstname": forms.TextInput(attrs={'class': 'p'}),
        "lastname": forms.TextInput(attrs={'class': 'p'}),
        "phone": forms.TextInput(attrs={'class': 'p'}),
        "joined_date": forms.DateInput(attrs={'class': 'p'}),
    }
