from django import forms
from .models import Task
class TaskForm(forms.Form):
    name=forms.CharField(max_length=100)
    desc=forms.CharField(widget=forms.Textarea)
    #created_at=forms.DateTimeField(widget=forms.DateTimeInput)
    #due_date=forms.DateTimeField(widget=forms.DateTimeInput)

class TaskForm_new(forms.ModelForm):
    class Meta:
        model=Task
        fields= '__all__'
        fields=('name','desc','due_date','list')
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }