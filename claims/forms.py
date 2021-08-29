from claims import widgets
from django import forms
from . import models


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"

    def __init__(self):
        super().__init__(format='%H:%M')


class ClaimsForms(forms.ModelForm):

    class Meta:
        model = models.Claims
        exclude = ('claim_status', 'user')
        widgets = {"date_accident": DateInput(),
                   "time_accident": TimeInput(), }
        input_formats = {"time_accident": "%I:%M %p"}
