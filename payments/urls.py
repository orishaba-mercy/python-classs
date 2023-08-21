from django.urls import path
from .views import payments_upload_view
from .views import payments_list
from .views import payments_details
from .views import payments_update_view
from .views import delete_payments

urlpatterns=[
    path('payments/upload' , payments_upload_view , name='payments_upload_view'),
    path("payments/list" ,payments_list,name="payments_list"),
    path("payments/<int:id>/", payments_details, name="payments_details"),
    path("payments/edit/<int:id>/", payments_update_view, name="payments_update_view"),
    path("paymenst/delete/ <int:id>/", delete_payments , name="delete_payments"),
]
