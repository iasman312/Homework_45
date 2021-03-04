from django import forms
from django.forms import widgets
from to_do_list.models import status_choices

class TaskForm(forms.Form):
    title = forms.CharField(max_length=120, required=True)
    status = forms.ChoiceField( required=True,
                               choices=status_choices, initial='new')
    up_to = forms.DateField(required=False)
    description = forms.CharField(max_length=1000, required=False,
                                  widget=widgets.Textarea)
