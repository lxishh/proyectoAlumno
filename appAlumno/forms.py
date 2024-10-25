from django import forms
from appAlumno.models import Alumno

class FormularioAlumno(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'