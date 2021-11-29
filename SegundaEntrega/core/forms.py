from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.forms import ModelForm
from .models import Insumos, Registros
import re

class InsumosForm(ModelForm):
    nombre= forms.CharField(min_length=3, max_length=120, required=True)
    precio= forms.IntegerField(min_value=1, required=True)
    descripcion= forms.CharField(min_length=3, max_length=200, widget=forms.Textarea(), required=False)
    stock= forms.IntegerField(min_value=0, required=True)

    class Meta:
        model= Insumos
        fields= ['nombre', 'precio', 'descripcion', 'stock']


class RegistrosForm(ModelForm):
        nombre = forms.CharField(min_length=3, max_length=80, required=True)
        apellido = forms.CharField(min_length=3, max_length=80, required=True)
        email = forms.CharField(required=True)
        username = forms.CharField(required=True)
        contraseña= forms.CharField(required=True)
        contraseña2= forms.CharField(required=True)

        class Meta:
                model=Registros
                fields= ['nombre', 'apellido', 'email' , 'username', 'contraseña', 'contraseña2']





helper = FormHelper()
helper.form_class = 'form-horizontal'
helper.layout = Layout(
        Field('textarea', rows='2',css_class='form-control')
)