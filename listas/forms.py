from django import forms
from .models import ListaDeseos, ListaRentados

class ListaDeseosCreate(forms.ModelForm):
    class Meta:
        model = ListaDeseos
        fields = ['usuario_id', 'libro_id']

class ListaRentadosCreate(forms.ModelForm):
    class Meta:
        model = ListaRentados
        fields = ['usuario_id', 'libro_id']