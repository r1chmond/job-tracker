from django import forms
from trackerapp.models import Status,Job, Note


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
    
        
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


