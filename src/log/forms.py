from django.forms import ModelForm
from .models import Temperature, Personnel
import datetime


class PersonnelForm(ModelForm):

    class Meta:
        model = Temperature
        fields = '__all__'


class UpdateForm(ModelForm):

    class Meta:
        model = Personnel
        fields = '__all__'
