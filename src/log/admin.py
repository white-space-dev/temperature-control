from django.contrib import admin
from . models import Personnel, Temperature, Department
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Personnel)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('name', 'rank', 'department', 'date_joined', 'date_signedoff')
    ordering = ('id',)
    search_fields = ('name', 'position')

    # class PersonnelAdmin(admin.ModelAdmin):


@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    list_display = ('date_temp_taken', 'user', 'temp_AM', 'temp_PM')
    ordering = ('-date_temp_taken',)
#admin.site.register(Temperature)

admin.site.register(Department)