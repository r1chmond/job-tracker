from django import forms
from trackerapp.models import Status,Job, Note
from bootstrap_datepicker_plus.widgets import DatePickerInput


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
            'date_applied':  DatePickerInput(options={'format': 'DD/MM/YYYY'}),
            'deadline':  DatePickerInput(options={'format': 'DD/MM/YYYY'}),
        }
    
        
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


