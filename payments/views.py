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


def payments_detail(request , id):
    payments= Payments.objects.get(id=id)
    return render(request , 'payments/payments_detail.html',{'payments':payments})




def customer_update_view(request, id):
    customer = Customer.objects.get(id=id)


    if request.method == 'POST':
        form = CustomerUploadForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect("customer_detail", id=customer.id)
    
    else:
        form = CustomerUploadForm(instance=customer)
        return render(request, "customer/edit_customer.html", {'form': form})

def delete_customer(request, id):
    customer= Customer.objects.get(id=id)
    customer.delete()
    return redirect("customer_list_view")