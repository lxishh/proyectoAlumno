from django.contrib import admin
from appAlumno.models import Alumno

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['dni', 'direccion', 'telefono', 'edad']

# Register your models here.
admin.site.register(Alumno, AlumnoAdmin)