from django.urls import path
from .views import order_upload_view
from .views import order_list
from .views import order_detail
from .views import order_update_view
from .views import delete_order

urlpatterns = [
    path('orders/upload',order_upload_view, name='order_upload_view'),
    path("orders/list", order_list , name="order_list"),
    path("orders/<int:id>/", order_detail, name="order_detail"),
    path("orders/edit/<int:id>/", order_update_view, name="order_update_view"),
    path("orders/delete/<int:id>/", delete_order , name="delete_order"),
]