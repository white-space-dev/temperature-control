from django.shortcuts import render
from django.http import HttpResponseRedirect
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

# Create your views here.


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
        context['temperature'] = person.temperature_set.all()[0:13]
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

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response



