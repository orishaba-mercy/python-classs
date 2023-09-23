
from django.urls import path
from .views import CustomerListView
from .views import CustomerDetailView
from.views import CartListView


urlpatterns = [
    # path("Customers/", CustomerListView.as_view(), name="customer_list_view"),
    path("customers/", CustomerListView.as_view(), name="customer_list_view"),
    path("Customer/<int:id>",CustomerDetailView.as_view(),name="customer_detail_view"),
    path("Cart/",CartListView.as_view(),name="Cart_list_view")
]