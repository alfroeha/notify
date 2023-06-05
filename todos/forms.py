from django import forms
from . models import Todo


class TodoForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=50)
    status = forms.ChoiceField(choices=Todo.STATUS_CHOICES)