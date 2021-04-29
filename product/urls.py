from django.urls import path
from .views import ItemList, ItemDetail

urlpatterns = [
    path('list/', ItemList.as_view()),
    path('<int:id>/', ItemDetail.as_view()),
]
