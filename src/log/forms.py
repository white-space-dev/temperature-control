from django.forms import ModelForm
from .models import Temperature
import datetime
import pytz


class PersonnelForm(ModelForm):

    class Meta:
        time_now = datetime.datetime.now().time()
        AM = datetime.time(6, 00, tzinfo=None)
        PM = datetime.time(12, 00, tzinfo=None)
        model = Temperature
        if PM >= time_now >= AM:  #find out how to get the hour
            fields = ('user', 'temp_AM')
        else:
            fields = ('user', 'temp_PM')



