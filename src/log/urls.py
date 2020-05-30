from django.urls import path
from .views import personnel_list,   department_view, html_to_pdf_view, PersonnelListView, PersonnelDetailView, \
    update_temp, add_temp, search
from .cron import missing_temp


urlpatterns = [
    path('', PersonnelListView.as_view(), name='list-view-all'),
    path('search/', search, name='search'),
    path('<int:pk>/', personnel_list, name='list-view'),
    path('dep/', department_view, name='department-view'),
    path('detailed_view/<int:pk>/', PersonnelDetailView.as_view(), name='detailed-view'),
    path('add_temp/<int:pk>/', add_temp, name='add-temperature'),
    path('update_temp/<int:pk>/', update_temp, name='update-temperature'),
    path('print/<int:pk>/', html_to_pdf_view, name='print'),
    path('missing', missing_temp, name='missing-temp')

]
