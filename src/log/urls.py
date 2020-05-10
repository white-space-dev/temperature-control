from django.urls import path
from .views import personnel_list, detailed_view, add_temp, department_view, html_to_pdf_view

urlpatterns = [
    path('', department_view, name='department-view'),
    path('<int:pk>/', personnel_list, name='list-view'),
    path('detailed_view/<int:pk>/', html_to_pdf_view, name='detailed-view'),
    path('add_temp/<int:pk>/', add_temp, name='add-temperature'),
]
