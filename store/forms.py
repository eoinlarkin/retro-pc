
from django import forms
from .models import Product, Cpu, Manufacturer, ReleaseDecade 


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

