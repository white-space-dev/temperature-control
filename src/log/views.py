import ssl

from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import Personnel, Department, Temperature, OIM, Medic
from .forms import PersonnelForm, UpdateForm
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


from django.conf import settings

from django.template.loader import render_to_string

from weasyprint.fonts import FontConfiguration


def personnel_list(request, pk):
    object_list = Personnel.objects.filter(department=pk)
    context = {
        'object_list': object_list
        }
    return render(request, 'log/front-page.html', context)


def search(request):
    query = request.GET.get('search').lower()
    object_list_all = Personnel.objects.all()
    object_list = [person for person in object_list_all if query in person.name.lower()]
    context = {
        'object_list': object_list
        }
    return render(request, 'log/search.html', context)


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
        context['oim'] = OIM.objects.get(id=1)
        context['medic'] = Medic.objects.get(id=1)
        return context


def add_temp(request, pk):
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


def personnel_update(request, pk):
    context = {}
    obj = get_object_or_404(Personnel, id=pk)
    form = UpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    context["form"] = form
    return render(request, 'log/personnel_update.html', context)


def update_temp(request, pk):
    context = {}
    obj = get_object_or_404(Temperature, user=pk, date_temp_taken=date.today())
    form = PersonnelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
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
    temperature = person.temperature_set.all()[0:14]
    oim = OIM.objects.get(id=1)
    medic = Medic.objects.get(id=1)

    context = {
        'person': person,
        'temperature': temperature,
        'oim': oim,
        'medic': medic
    }
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = "attachment; filename ='mypdf.pdf'"
    html = render_to_string('log/personnel-detail.html', context)
    font_config = FontConfiguration()
    HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response, font_config=font_config, presentational_hints=True)
    return response




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