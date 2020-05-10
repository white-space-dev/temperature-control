from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import Personnel, Department
from .forms import PersonnelForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML

# Create your views here.


def personnel_list(request, pk):
    if pk == 0:
        qs = Personnel.objects.all()
        context = {
            'qs': qs
        }
    else:
        qs = Personnel.objects.filter(department=pk)
        context = {
            'qs': qs
        }
    return render(request, 'log/front-page.html', context)


def detailed_view(request, pk):
    person = Personnel.objects.get(pk=pk)
    temp = person.temperature_set.all()

    context = {
        'person': person,
        'temp': temp

    }
    return render(request, 'log/personnel-detail.html', context)


def add_temp(request, pk):
    qs_name = {'department': [], 'user': [pk], 'temp': [], 'time_temp_taken': []}
    submitted = False
    if request.method == 'POST':
        form = PersonnelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_temp/{}?submitted=True'.format(pk))
    else:
        form = PersonnelForm(qs_name)
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'log/add_temp.html', {'form': form, 'submitted': submitted})


def department_view(request):
    qs = Department.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'log/department-view.html', context)


def html_to_pdf_view(request):
    html_string = render_to_string('log/personnel-detail.html')

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response