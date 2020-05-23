from django.forms import ModelForm
from .models import Temperature
import datetime



class PersonnelForm(ModelForm):

    class Meta:
        model = Temperature
        fields = '__all__'




