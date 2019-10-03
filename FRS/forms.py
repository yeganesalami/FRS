from django.forms import ModelForm
from FRS.models import Flight


class FlightForm(ModelForm):
    class Meta:
        model = Flight