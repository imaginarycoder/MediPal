from django import forms
from application.models import Subscribers

class NewSubscriberForm(forms.ModelForm):
    #email = forms.EmailField()
    class Meta():
        model = Subscribers
        fields = '__all__'

"""
class NewSubscriberForm(forms.Form):
    email = forms.EmailField()
"""
