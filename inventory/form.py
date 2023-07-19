from django import forms
from models import Product

class ProductUploadForm(forms.ModelForm):
    class Meta:
        model = Product
        fiels="__all__"
        


