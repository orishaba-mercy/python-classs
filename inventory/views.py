from django.shortcuts import render
from .form import ProductUploadForm

# Create your views here.
def Product_upload_views(request):
    form = ProductUploadForm()
    return render(request,"Product/Product_upload.html" , {'form':form})
