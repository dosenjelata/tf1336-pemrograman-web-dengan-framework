from django import forms
from django.forms import ModelForm

from .models import Question

class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=200)
    pub_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))




class QuestionModelForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
            'pub_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }