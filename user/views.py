    from rest_framework import exceptions, status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserCreateSerializer, ProfileSerializer
from .models import Profile, User
from .utils_token import generate_token, generate_refresh_token, new_token_after_refresh


class Register(CreateAPIView):
    """
        Register user
    """
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny,]


class Login(APIView):
    """
        Login user
    """
    permission_classes = [AllowAny,]

    @staticmethod
    def post(request):
        username = request.data['username']
        password = request.data['password']

        if (username is None) or (password is None):
            response_data = {
                "msg": "Username and password are required fields"
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(username=username).first()

        if user is None:
            raise exceptions.AuthenticationFailed("User not found")

        if user.check_password(password):
            response = Response()

            response.data = {
                "access_token": generate_token(user),
                "refresh_token": generate_refresh_token(user)
            }
            return response


class RefreshToken(APIView):
    """
        Refresh token after expired
    """
    permission_classes = [AllowAny, ]

    @staticmethod
    def post(request):
        refresh_token = request.data.get("refresh_token")

        if refresh_token is None:
            raise exceptions.AuthenticationFailed("Refresh token is not provided")

        response_data = {
            "access_token": new_token_after_refresh(refresh_token)
        }
        return Response(response_data, status=status.HTTP_200_OK)


class GetOrEditProfile(APIView):
    """
        Get user profile if not exist create new one
    """
    @staticmethod
    def get(request):
        user_profile = Profile.objects.filter(user=request.user)
        profile = user_profile.first() if user_profile.exists() else Profile.objects.create(user=request.user)
        profile_serialize = ProfileSerializer(profile)
        return Response(profile_serialize.data, 200)

    @staticmethod
    def put(request):
        profile = Profile.objects.filter(user=request.user).first()
        profile_serialize = ProfileSerializer(profile, request.data)
        profile_serialize.is_valid(raise_exception=True)
        profile_serialize.save()
        return Response(profile_serialize.data, 200)





"""
MultipleFieldLookupMixin: custom mixin

Viewsets
GenericViewSet
ModelViewSet
ReadOnlyModelViewSet

Router

ModelViewSet extra action
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
