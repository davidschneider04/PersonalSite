import calendar

from django import forms
from dal import autocomplete

from . import views
from .models import PTFormInput

class ParkingTicketForm(forms.ModelForm):
    day_of_week = autocomplete.Select2ListChoiceField(choice_list=list(calendar.day_name))#, widget=autocomplete.ListSelect2(url='dsp:ptform-options-autocomplete'))
    week_of_month = autocomplete.Select2ListChoiceField(choice_list=['1st','2nd','3rd','4th'])#, widget=autocomplete.ListSelect2(url='dsp:ptform-options-autocomplete'))
    class Meta:
        model = PTFormInput
        fields = ('week_of_month', 'day_of_week',)
        widgets = {
        	'week_of_month': autocomplete.ListSelect2(url='dsp:ptform-options-autocomplete'),
            'day_of_week': autocomplete.ListSelect2(url='dsp:ptform-options-autocomplete'),
        }