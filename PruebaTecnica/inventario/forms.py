from django import forms
from .models import Producto
from django import forms

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
