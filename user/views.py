from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import UserCreateSerializer


class Register(CreateAPIView):
    serializer_class = UserCreateSerializer


class Login(ObtainAuthToken):
    pass



"""
GenericApiView and methods
perform_create
ListApiView
Mixins: ListModelMixin CreateModelMixin RetrieveModelMixin UpdateModelMixin DestroyModelMixin
ConcreteViewClasses: CreateApiView ListApiView RetrieveApiView UpdateApiView DestroyApiView
ListCreateApiView RetrieveUpdateApiView RetrieveDestroyApiView 
RetrieveUpdateDestroyApiView

lookup_fields
MultipleFieldLookupMixin: custom mixin

Viewsets
GenericViewSet
ModelViewSet
ReadOnlyModelViewSet

Router

ModelViewSet extra action

Nested Serializer
PrimaryKeyRelatedField
Other related fields

HyperlinkedModelSerializer

"""

"""
Tasks
----------------------------
1. Token Auth
2. Create Models
3. Serializers
4. Generic Views
5. Viewsets

----------------------------
"""
