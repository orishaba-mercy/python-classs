from django.urls import path
from .views import cart_upload_view
from .views import cart_list
from .views import cart_detail
from .views import cart_update_view
from .views import delete_cart

urlpatterns=[
    path('carts/upload' , cart_upload_view , name='cart_upload_view'),
    path("carts/list" ,cart_list,name="cart_list"),
    path("carts/<int:id>/", cart_detail, name="cart_detail"),
    path("carts/edit/<int:id>/", cart_update_view, name="cart_update_view"),
    path("carts /delete/ <int:id>/", delete_cart , name="delete_cart"),
]
 



