from django.urls import path
from .views import Register, Login, RefreshToken, GetOrEditProfile

urlpatterns = [
    path("sign-up/", Register.as_view(), name="signup"),
    path('sign-in/', Login.as_view(), name="sign"),
    path("refresh-token/", RefreshToken.as_view(), name="refresh-token"),
    path('profile/', GetOrEditProfile.as_view(), name="profile"),
]
