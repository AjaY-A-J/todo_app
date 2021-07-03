from .models import Task
from django import forms
class Todoforms(forms.ModelForm):
    class meta:
        model=Task
        fields=['name','priority','date']