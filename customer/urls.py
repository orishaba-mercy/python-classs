
from django.urls import path
from .views import customer_upload_view
from .views import customer_list
from .views import customer_detail
from .views import customer_update_view
from .views import delete_customer

urlpatterns=[
    path('customers/upload' , customer_upload_view , name='customer_upload_view'),
    path("customers/list" ,customer_list,name="customer_list"),
    path("customers/<int:id>/", customer_detail, name="customer_detail"),
    path("customers/edit/<int:id>/", customer_update_view, name="customer_update_view"),
    path("customers/delete/ <int:id>/", delete_customer , name="delete_customer"),
]
