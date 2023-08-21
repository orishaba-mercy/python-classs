from django.shortcuts import render,redirect
from .forms import PaymentsUploadForm
from .models import Payments


# Create your views here.
def payments_upload_view(request):
    if request.method =="POST" :
        form= PaymentsUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PaymentsUploadForm()
        
    return render(request, 'payments/payments_upload.html', {'form': form})


def payments_list(request):
    payments = Payments.objects.all()
    return render(request, 'payments/payments_list.html', {'payments':payments})


def payments_details(request , id):
    payments= Payments.objects.get(id=id)
    return render(request ,'payments/payments_details.html',{'payments':payments})


def payments_update_view(request, id):
    payments=Payments.objects.get(id=id)
    if request.method == 'POST':
        form = PaymentsUploadForm(request.POST, instance=payments)

        if form.is_valid():
            form.save()
            return redirect("payments_details", id=id)
    
    else:
        form = PaymentsUploadForm(instance=payments)
        return render(request, "payments/edit_payments.html", {'form': form})

def delete_payments(request, id):
    payments= payments.objects.get(id=id)
    payments.delete()
    return redirect("payments_list_view")