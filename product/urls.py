from django.urls import path
from .views import ItemList, ItemDetail, CategoryList

urlpatterns = [
    path('list/', ItemList.as_view(), name="item-list"),
    path('<int:id>/', ItemDetail.as_view(), name="item-detail"),
    path('category-list/', CategoryList.as_view(), name="category-list")
]
