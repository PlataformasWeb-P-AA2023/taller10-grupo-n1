from django.forms import ModelForm
from django import forms

from ordenamiento.models import *

class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'tipo'] 

class BarrioForm(ModelForm):

    def __init__(self, parroquia, *args, **kwargs):
        super(BarrioForm, self).__init__(*args, **kwargs)
        self.initial['parroquia'] = parroquia
        self.fields["parroquia"].widget = forms.widgets.HiddenInput()
        print(parroquia)

    class Meta:
        model = Barrio
        fields = ['nombre', 'viviendas', 'num_parques', 'edificios', 'parroquia']


class BarrioEditForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'viviendas', 'num_parques', 'edificios']
