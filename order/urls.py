from django.urls import path
from .views import ListOrders, CreateOrder, RetrieveUpdateDestroyOrder

urlpatterns = [
    path("list/", ListOrders.as_view(), name="list-orders"),
    path("create/", CreateOrder.as_view(), name="create-order"),
    path("update/", RetrieveUpdateDestroyOrder.as_view(), name="update-order"),

]
