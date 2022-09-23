
from  django import forms 
from revista.models import Articulos

class ArticuloForm(forms.ModelForm):
    class Meta:
        model= Articulos
        fields = '__all__'

       