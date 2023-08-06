from django.urls import path
from .views import cart_upload_views

urlpatterns=[
    path('carts/upload' , cart_upload_views , name='cart_upload_view'),
]
