from django.forms import ModelForm
from .models import Consumption


class ConsumptionForm(ModelForm):
    class Meta:
        model = Consumption
        fields = ['date', 'time']
