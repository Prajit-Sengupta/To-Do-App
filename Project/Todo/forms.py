#Form representation of a model
from django import forms
from django.forms import ModelForm


from .models import * 

class TaskForm(forms.ModelForm):

    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'})) #this statemnet is just to add a placeholder to put in title field iof model

    class Meta:
        model = Task #Two info needed in meta , for which model we re making the form and what fields will we allow
        fields = '__all__'