from django.shortcuts import render
from .forms import CartUploadForm

# Create your views here.
def cart_upload_views(request):
    form = CartUploadForm()
    return render(request,"cart/cart_upload.html" , {'form':form})
