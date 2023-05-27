from django import forms
from . models import DAY_CHOICES


class CourseForm(forms.Form):
    name = forms.CharField(max_length=255)
    room = forms.CharField(max_length=50)
    day = forms.ChoiceField(choices=DAY_CHOICES)