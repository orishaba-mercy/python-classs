from django.urls import path
from .views import cart_upload_views

urlpatterns=[
    path('cart/upload' , cart_upload_views , name='cart_upload_views'),
]