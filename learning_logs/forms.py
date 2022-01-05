from django import forms
from django.forms import widgets
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic #build a form from topic model and include only text field
        fields = ['text']
        labels = {'text': ''} #tells django not to generate a label for the text field

class EntryForm(forms.ModelForm):
    class Meta: #nested meta class listing model it's based on
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry'} 
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} #widgets is an HTML form element. We can override django's default widget choice. We customize input widget for field 'text'