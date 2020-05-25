import ssl

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . models import Personnel, Department, Temperature
from .forms import PersonnelForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404
from random import uniform
from django.urls import reverse_lazy
from datetime import date

from weasyprint import HTML
import functools
from django_weasyprint import WeasyTemplateResponseMixin, WeasyTemplateResponse
from django.conf import settings

from django.template.loader import render_to_string

from weasyprint.fonts import FontConfiguration



def personnel_list(request, pk):
    object_list = Personnel.objects.filter(department=pk)
    context = {
        'object_list': object_list
        }
    return render(request, 'log/front-page.html', context)

class PersonnelListView(ListView):
    model = Personnel
    template_name = 'log/front-page.html'



'''def detailed_view(request, pk):
    person = Personnel.objects.get(pk=pk)
    temp = person.temperature_set.all()

    context = {
        'person': person,
        'temp': temp

    }
    return render(request, 'log/personnel-detail.html', context)'''

class PersonnelDetailView(DetailView):
    model = Personnel
    template_name = 'log/personnel-detail.html'


    '''def get_queryset(self): 
        print(self.request)
        username = self.name
        self.user = get_object_or_404(Personnel, pk=self.kwargs['pk'])
        return Temperature.objects.filter(user=self.user)'''

    def get_context_data(self, **kwargs):
        person = Personnel.objects.get(pk=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['person'] = person
        context['temperature'] = person.temperature_set.all()[0:14]
        return context

def add_temp(request, pk):
    #qs_name = {'department': [], 'user': [pk], 'temp': [], 'time_temp_taken': []}
    submitted = False
    if request.method == 'POST':
        form = PersonnelForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_temp/{}?submitted=True'.format(pk))
    else:
        form = PersonnelForm(initial={'user': pk})
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'log/add_temp.html', {'form': form, 'submitted': submitted})


'''class CreateTemperature(CreateView):
    model = Temperature

    #fields = ['temp_AM']
   # queryset =
    form_class = PersonnelForm
    success_url = reverse_lazy('list-view-all')
    template_name = 'log/add_temp.html'

    #def get_object(self, queryset=None):
        #return Personnel.objects.get(id=self.pk)

    def get_initial(self):
        self.initial = {'user': self.pk}
        return self.initial'''



'''class UpdateTemperature(UpdateView):
    model = Temperature
    #initial = {'temp_AM': Temperature.objects.get(user=pk, date_temp_taken=date.today()).temp_AM }
    success_url = reverse_lazy('list-view-all')
    fields = ['user', 'temp_AM', 'temp_PM', 'date_temp_taken']
    template_name = 'log/update_temp.html'

    def get_queryset(self):
        self.user = get_object_or_404(Personnel, id=self.kwargs['pk']).id
        return Temperature.objects.filter(date_temp_taken=date.today(), user=self.user)

    def get_initial(self):
        person = Temperature.objects.get(user=self.kwargs['pk'], date_temp_taken=date.today())
        self.initial = {'user': self.kwargs['pk'], 'temp_AM': person.temp_AM}
        return (self.initial)

    def get_object(self, queryset=None):
        return'''


def update_temp(request, pk):
    context = {}
    obj = get_object_or_404(Temperature, user=pk, date_temp_taken=date.today())
    form = PersonnelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/list/')
    context["form"] = form
    return render(request, 'log/update_temp.html', context)


def department_view(request):
    qs = Department.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'log/department-view.html', context)


def html_to_pdf_view(request, pk):
    person = Personnel.objects.get(pk=pk)
    temperature = person.temperature_set.all()

    context = {
        'person': person,
        'temperature': temperature

    }
    html_string = render_to_string('log/personnel-detail.html', context)

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/mypdf.pdf', presentational_hints=True);

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response

#from __future__ import unicode_literals

'''def temperature_record(request, pk):
    person = get_object_or_404(Personnel, pk=pk)
    temperature = person.temperature_set.all()

    context = {
        'person': person,
        'temperature': temperature

    }

    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    html = render_to_string("log/personnel-detail.html", context)

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)
    return response'''






'''class CustomWeasyTemplateResponse(WeasyTemplateResponse):
    # customized response class to change the default URL fetcher
    def get_url_fetcher(self):
        # disable host and certificate check
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return functools.partial(django_url_fetcher, ssl_context=context)

class MyModelPrintView(WeasyTemplateResponseMixin, PersonnelDetailView):
    # output of MyModelView rendered as PDF with hardcoded CSS
    #pdf_stylesheets = [
        #settings.STATICFILES_DIRS[0] + 'css/app.css',]
    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = True
    # custom response class to configure url-fetcher
    #response_class = CustomWeasyTemplateResponse

class MyModelDownloadView(WeasyTemplateResponseMixin, PersonnelDetailView):
    # suggested filename (is required for attachment/download!)
    pdf_filename = 'mypdf.pdf' '''