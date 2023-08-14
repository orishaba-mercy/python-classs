from django.urls import path
from .views import payments_upload_view
from .views import payments_list
from .views import payments_detail
from .views import payments_update_view
from .views import delete_payments

urlpatterns=[
    path('payment/upload' , payments_upload_view , name='payments_upload_view'),
    path("payment/list" ,payments_list,name="payments_list"),
    path("payment/<int:id>/", payments_detail, name="payments_detail"),
    path("payment/edit/<int:id>/", payments_update_view, name="payments_update_view"),
    path("payment/delete/ <int:id>/", delete_payments , name="delete_payments"),
]
